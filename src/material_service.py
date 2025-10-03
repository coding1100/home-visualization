import os
import time
import json
import base64
import uuid
from typing import Dict, Optional, Tuple

import cv2
import requests
import numpy as np
from fastapi import HTTPException, UploadFile

from app.modules.files.s3utils.s3_utils import s3_upload_file
from src.logger import logger
from src.constants import _MB_DIVISOR, DEFAULT_EXCLUDE_TYPES, MATERIAL_PROMINENCE, UPLOAD_DIR
from src.cloudinary_func import ensure_cloudinary_config, upload_image_to_cloudinary
from app.modules.catalog.data.product_images import PRODUCT_IMAGE_MAP  # same place your FileService pulls config from

def _calc_edge_margin_px(H: int, W: int) -> int:
    """Derive a dilation size that scales with image resolution."""
    return max(0, int(round(min(H, W) * 0.000)))  # ~0.6% of shorter side

def _calc_erosion_px(H: int, W: int) -> int:
    """Derive an erosion size that scales with image resolution."""
    return max(1, int(round(min(H, W) * 0.002)))  # ~0.2% of shorter side

def _normalize_poly(coords):
    """Normalize polygon coordinates to a consistent format."""
    out = []
    for pt in coords or []:
        if isinstance(pt, dict):
            out.append([float(pt.get("x", pt.get("X"))), float(pt.get("y", pt.get("Y")))])
        elif isinstance(pt, (list, tuple)) and len(pt) >= 2:
            out.append([float(pt[0]), float(pt[1])])
    return out

def _poly_to_mask(coords, H, W):
    """Convert polygon coordinates to a binary mask."""
    pts = _normalize_poly(coords)
    m = np.zeros((H, W), np.uint8)
    if len(pts) >= 3:
        pts_i = np.round(np.array(pts, dtype=np.float32)).astype(np.int32).reshape(-1,1,2)
        cv2.fillPoly(m, [pts_i], 255)
    return m

def _union_mask(elements, match_types, H, W):
    """Create a union mask from elements matching the specified types."""
    m = np.zeros((H, W), np.uint8)
    for e in elements or []:
        t = (e.get("type") or e.get("class") or "").lower()
        if t in match_types:
            coords = e.get("coordinates") or e.get("polygon")
            if coords:
                m = cv2.bitwise_or(m, _poly_to_mask(coords, H, W))
    return m

def _union_mask_except(elements, target_ids, target_types, H, W):
    """Mask union of all elements except the provided ids/types."""
    m = np.zeros((H, W), np.uint8)
    id_set = {str(i) for i in (target_ids or []) if i is not None}
    type_set = {t for t in (target_types or []) if t}
    for e in elements or []:
        eid = e.get("id")
        etype = (e.get("type") or e.get("class") or "").lower().strip()
        if id_set and str(eid) in id_set:
            continue
        if type_set and etype in type_set:
            continue
        coords = e.get("coordinates") or e.get("polygon")
        if coords:
            m = cv2.bitwise_or(m, _poly_to_mask(coords, H, W))
    return m

def _elements_to_mask(elements, H, W, include_ids=None, include_types=None):
    """Build union mask for elements matching provided ids/types."""
    id_set = {str(i).lower() for i in (include_ids or []) if i is not None}
    type_set = {t.lower() for t in (include_types or []) if t}
    m = np.zeros((H, W), np.uint8)
    for e in elements or []:
        eid = e.get("id").lower()
        etype = (e.get("type") or e.get("class") or "").lower().strip()
        if id_set and str(eid) not in id_set:
            continue
        if type_set and etype not in type_set:
            continue
        coords = e.get("coordinates") or e.get("polygon")
        if coords:
            m = cv2.bitwise_or(m, _poly_to_mask(coords, H, W))
    return m

def build_selection_mask(
    elements,
    H,
    W,
    include_ids=None,
    include_types=None,
    exclude_types=None,
    exclude_ids=None,
    edge_margin_px=3,
    erosion_px=1,
    remove_other_geometry=False,
):
    """Construct a stable mask for the requested selection."""
    include_mask = _elements_to_mask(elements, H, W, include_ids, include_types)
    if np.count_nonzero(include_mask) == 0:
        return include_mask

    exclude_mask = np.zeros((H, W), np.uint8)
    if exclude_types:
        exclude_mask = cv2.bitwise_or(exclude_mask, _union_mask(elements, exclude_types, H, W))
    if exclude_ids:
        exclude_mask = cv2.bitwise_or(exclude_mask, _elements_to_mask(elements, H, W, include_ids=exclude_ids))
    if remove_other_geometry:
        exclude_mask = cv2.bitwise_or(
            exclude_mask,
            _union_mask_except(elements, include_ids, include_types, H, W)
        )

    if edge_margin_px > 0 and np.count_nonzero(exclude_mask) > 0:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*edge_margin_px+1, 2*edge_margin_px+1))
        exclude_mask = cv2.dilate(exclude_mask, k, 1)

    refined = cv2.bitwise_and(include_mask, cv2.bitwise_not(exclude_mask))

    if erosion_px > 0:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*erosion_px+1, 2*erosion_px+1))
        refined = cv2.erode(refined, k, 1)

    refined = cv2.morphologyEx(refined, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), 1)
    return refined

def build_refined_mask(elements, target_types, exclude_types, H, W, edge_margin_px=2):
    """Build refined mask: (Union of target_types) minus (grown union of exclude_types)."""
    inc = _union_mask(elements, target_types, H, W)
    exc = _union_mask(elements, exclude_types, H, W)
    if edge_margin_px > 0:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*edge_margin_px+1, 2*edge_margin_px+1))
        exc = cv2.dilate(exc, k, 1)
    refined = cv2.bitwise_and(inc, cv2.bitwise_not(exc))
    # small open to clean mask specks
    refined = cv2.morphologyEx(refined, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), 1)
    return refined

def _calculate_element_specific_scale(element: Dict, image_height: int, image_width: int) -> float:
    """
    Calculate element-specific scale based on element dimensions and type.
    
    Args:
        element: Element dictionary with coordinates and type
        image_height: Total image height in pixels
        image_width: Total image width in pixels
        
    Returns:
        Calculated scale factor for texture tiling
    """
    # Get element coordinates
    coords = element.get("coordinates", [])
    if not coords:
        return 1.0  # Default scale if no coordinates
    
    # Calculate element bounding box
    x_coords = [point["x"] for point in coords]
    y_coords = [point["y"] for point in coords]
    
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    element_width = max_x - min_x
    element_height = max_y - min_y
    element_area = element_width * element_height
    
    # Calculate element area relative to total image area
    total_area = image_width * image_height
    element_area_ratio = element_area / total_area
    
    # Get element type for type-specific scaling
    element_type = (element.get("type") or element.get("class") or "").lower().strip()
    
    # Type-specific scaling factors (smaller elements need smaller tiles)
    type_scaling_factors = {
        "window": 0.3,      # Windows are typically small, need fine detail
        "door": 0.4,        # Doors are medium-small
        "garage": 0.6,      # Garages are larger
        "wall": 0.8,        # Walls are large
        "roof": 1.0,        # Roofs can be very large
        "trim": 0.2,        # Trim/moldings are very small
        "siding": 0.7,      # Siding is medium-large
    }
    
    # Get type-specific factor (default to 0.5 for unknown types)
    type_factor = type_scaling_factors.get(element_type, 0.5)
    
    # Calculate scale based on element size and type
    # Larger elements relative to image get larger scale values
    size_factor = max(0.1, min(2.0, element_area_ratio * 10))  # Clamp between 0.1 and 2.0
    
    # Combine type and size factors
    calculated_scale = type_factor * size_factor
    
    # Final bounds to prevent unrealistic scaling
    final_scale = max(0.1, min(3.0, calculated_scale))
    
    logger.info(f"Element scale calculation: type={element_type}, area_ratio={element_area_ratio:.4f}, "
                f"type_factor={type_factor}, size_factor={size_factor:.2f}, final_scale={final_scale:.2f}")
    
    return final_scale

def _encode_output_image(
    image: np.ndarray,
    compression_levels: Tuple[int, int] = (3, 9),
) -> Tuple[str, float, Tuple[int, int], bool]:
    """
    Encode an image to base64.

    Args:
        image: BGR image to encode.
        compression_levels: (default_png_compression, high_png_compression).

    Returns:
        Tuple containing (base64 string, size in MB, (width, height), was_downscaled).

    Raises:
        HTTPException: If encoding fails.
    """

    if image is None or image.size == 0:
        raise HTTPException(status_code=500, detail="Output image is empty")

    default_comp, _ = compression_levels

    def _encode(image_to_encode: np.ndarray, compression: int) -> bytes:
        success, buffer = cv2.imencode('.png', image_to_encode, [cv2.IMWRITE_PNG_COMPRESSION, compression])
        if not success:
            raise HTTPException(status_code=500, detail="Failed to encode output image")
        return buffer.tobytes()

    encoded_bytes = _encode(image, default_comp)
    size_mb = len(encoded_bytes) / _MB_DIVISOR

    b64_image = base64.b64encode(encoded_bytes).decode('utf-8')
    return b64_image, size_mb, (image.shape[1], image.shape[0]), False

# ====== TEXTURE UTILS ======
def reinhard_match(src_bgr, ref_bgr, mask=None):
    """Apply Reinhard color transfer in Lab color space."""
    # very lightweight color transfer in Lab (preserve src contrast)
    src = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    ref = cv2.cvtColor(ref_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    if mask is not None:
        m = (mask>0)
        if np.count_nonzero(m)==0: return src_bgr
        s_mu, s_sd = src[m].mean(axis=0), src[m].std(axis=0)+1e-6
        r_mu, r_sd = ref[m].mean(axis=0), ref[m].std(axis=0)+1e-6
    else:
        s_mu, s_sd = src.reshape(-1,3).mean(0), src.reshape(-1,3).std(0)+1e-6
        r_mu, r_sd = ref.reshape(-1,3).mean(0), ref.reshape(-1,3).std(0)+1e-6
    out = (src - s_mu)/s_sd * r_sd + r_mu
    out = np.clip(out, 0, 255).astype(np.uint8)
    return cv2.cvtColor(out, cv2.COLOR_LAB2BGR)

def tile_texture(tex_bgr, canvas_hw, scale=1.0, angle_deg=0.0):
    """Tile texture with scaling and rotation for even distribution."""
    Hc, Wc = canvas_hw
    h, w = tex_bgr.shape[:2]
    
    # Ensure minimum tile size for consistent coverage
    min_tile_size = 32
    scale = max(scale, min_tile_size / min(h, w))
    
    # scale
    new_w = max(1, int(w*scale)); new_h = max(1, int(h*scale))
    tex = cv2.resize(tex_bgr, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
    
    # rotate
    M = cv2.getRotationMatrix2D((new_w/2, new_h/2), angle_deg, 1.0)
    tex = cv2.warpAffine(tex, M, (new_w, new_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    
    # tile with better edge handling for even distribution
    tiles_x = int(np.ceil(Wc/new_w)) + 2  # Extra tiles for seamless coverage
    tiles_y = int(np.ceil(Hc/new_h)) + 2
    tiled = np.tile(tex, (tiles_y, tiles_x, 1))
    
    # Center the tiling to avoid edge artifacts
    start_y = (tiles_y * new_h - Hc) // 2
    start_x = (tiles_x * new_w - Wc) // 2
    tiled = tiled[start_y:start_y+Hc, start_x:start_x+Wc]
    
    return tiled

def _auto_angle_from_cnt(cnt):
    """Extract angle from contour for automatic orientation."""
    rect = cv2.minAreaRect(cnt)  # angle in [-90,0)
    angle = rect[2]; (w,h) = rect[1]
    if w < h: angle += 90
    return float(angle)

def apply_texture_cv_poisson(
    original_bgr, mask, texture_bgr,
    scale=1.0, angle_deg=0.0,
    color_match=None, preserve_shading=True,
    material_prominence=0.8, pad=16, erosion_px=1, clone_mode=cv2.MIXED_CLONE
):
    """Apply texture using OpenCV Poisson blending."""
    H, W = original_bgr.shape[:2]
    mask_bin = (mask > 0).astype(np.uint8)
    if np.count_nonzero(mask_bin) == 0:
        return original_bgr

    # color match (optional)
    if color_match == "reinhard":
        region = original_bgr.copy(); region[mask_bin==0] = 0
        texture_bgr = reinhard_match(texture_bgr, region, mask=mask_bin)

    # Create even texture coverage across the entire mask area
    canvas_size = (max(H,W), max(H,W))
    tiled = tile_texture(texture_bgr, canvas_size, scale=scale, angle_deg=angle_deg)
    
    # Use simpler, more even transformation for consistent coverage
    ys, xs = np.where(mask_bin>0)
    if len(xs) == 0:
        return original_bgr
        
    # Get bounding box of mask for more even coverage
    x_min, x_max = np.min(xs), np.max(xs)
    y_min, y_max = np.min(ys), np.max(ys)
    
    # Create a more uniform texture mapping
    # Use affine transformation instead of perspective for more even distribution
    src_points = np.float32([[0, 0], [canvas_size[1]-1, 0], [canvas_size[1]-1, canvas_size[0]-1]])
    dst_points = np.float32([[x_min, y_min], [x_max, y_min], [x_max, y_max]])
    
    try:
        Hmat = cv2.getAffineTransform(src_points, dst_points)
        src_warp = cv2.warpAffine(tiled, Hmat, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    except cv2.error:
        # Fallback to simple resize if affine fails
        src_warp = cv2.resize(tiled, (W, H), interpolation=cv2.INTER_CUBIC)

    if preserve_shading:
        lab_o = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
        lab_s = cv2.cvtColor(src_warp,     cv2.COLOR_BGR2LAB).astype(np.float32)
        L_orig = lab_o[..., 0]
        L_tex  = lab_s[..., 0]
        a_s, b_s = lab_s[...,1], lab_s[...,2]

        mask_f = (mask_bin.astype(np.float32) / 255.0)
        # Calculate shading_keep based on material_prominence (0.8 = 80% material, 20% original)
        shading_keep = 1.0 - material_prominence  # material_prominence=0.8 -> shading_keep=0.2
        L_mix = L_tex * (1.0 - shading_keep) + L_orig * shading_keep
        L = L_orig * (1.0 - mask_f) + L_mix * mask_f

        src_warp = cv2.cvtColor(np.dstack([L, a_s, b_s]).astype(np.uint8), cv2.COLOR_LAB2BGR)

    # crop ROI + safe center
    x,y,w,h = cv2.boundingRect(np.column_stack([xs,ys]).astype(np.int32))
    x0,y0 = max(0,x-pad), max(0,y-pad)
    x1,y1 = min(W,x+w+pad), min(H,y+h+pad)
    roi_dst  = original_bgr[y0:y1, x0:x1]
    roi_src  = src_warp    [y0:y1, x0:x1]
    roi_mask = mask_bin    [y0:y1, x0:x1]
    if roi_dst.size == 0 or np.count_nonzero(roi_mask)==0:
        return original_bgr
    roi_mask_u8 = (roi_mask>0).astype(np.uint8)*255
    if erosion_px>0:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*erosion_px+1, 2*erosion_px+1))
        roi_mask_u8 = cv2.erode(roi_mask_u8, k, 1)

    M = cv2.moments(roi_mask_u8, True)
    if M["m00"]>0:
        cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
    else:
        cx, cy = roi_dst.shape[1]//2, roi_dst.shape[0]//2
    cx = int(np.clip(cx, 0, roi_dst.shape[1]-1)); cy = int(np.clip(cy, 0, roi_dst.shape[0]-1))

    # Use controlled alpha blending for more even results
    alpha = (roi_mask_u8.astype(np.float32)/255.0)[...,None]
    
    # Apply material prominence to the alpha channel for more control
    alpha_adjusted = alpha * material_prominence
    
    # Smooth blending with controlled opacity
    blended_roi = (roi_src * alpha_adjusted + roi_dst * (1.0 - alpha_adjusted)).astype(np.uint8)

    out = original_bgr.copy()
    out[y0:y1, x0:x1] = blended_roi
    return out

def apply_texture_per_region(original, union_mask, texture, scale=1.0, angle_mode="auto",
                             angle_bias_deg=90.0, color_match=None, preserve_shading=True, material_prominence=0.8):
    """Clone per connected wall (stable angles, avoids cross-bleed)."""
    out = original.copy()
    cnts, _ = cv2.findContours(union_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        sub = np.zeros_like(union_mask); cv2.drawContours(sub, [c], -1, 255, -1)
        # Reapply original mask to preserve interior holes (windows, doors, etc.)
        sub = cv2.bitwise_and(sub, union_mask)
        a = _auto_angle_from_cnt(c) if angle_mode=="auto" else float(angle_mode)
        a = float(a) + float(angle_bias_deg)
        out = apply_texture_cv_poisson(out, sub, texture, scale=scale, angle_deg=a,
                                       color_match=color_match, preserve_shading=preserve_shading,
                                       material_prominence=material_prominence)
    return out

def download_material_image_binary(material_id: str) -> bytes:
    """
    Download material image from URL and return binary data directly.
    Eliminates the need for temporary files.
    """
    # Check if material_id exists in PRODUCT_IMAGE_MAP
    if material_id not in PRODUCT_IMAGE_MAP:
        available_ids = list(PRODUCT_IMAGE_MAP.keys())[:10]  # Show first 10 for reference
        raise HTTPException(
            status_code=400, 
            detail=f"Material ID '{material_id}' not found in catalog. Available IDs include: {available_ids}"
        )
    # Get the image URL
    image_url = PRODUCT_IMAGE_MAP[material_id]    
    try:
        # Download the image directly to memory
        logger.info(f"Downloading material image from: {image_url}")
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        logger.info(f"Material image downloaded successfully ({len(response.content)} bytes)")
        return response.content
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download material image from {image_url}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to download material image: {str(e)}")
    except Exception as e:
        logger.error(f"Error downloading material image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error downloading material image: {str(e)}")

def advanced_material_replacement(
    original_image: str,
    mask_image: Optional[str] = None,
    elements_json: Optional[str] = None,
    element_type: Optional[str] = None,
    element_id: Optional[str] = None,
    material_image: Optional[UploadFile] = None,
    material_id: Optional[str] = None,
    method: str = "cv_poisson",
    scale: float = 1.0,
    angle_bias_deg: float = 90.0,
    color_match: Optional[str] = None,
    preserve_shading: int = 0,
    material_prominence: float = MATERIAL_PROMINENCE,
    response_mode: str = "base64",

):
    """
    Advanced material replacement with cv_poisson method.
    
    Args:
        original_image: URL of the original image to process
        mask_image: Base64 encoded mask image (optional)
        elements_json: JSON string of house elements (optional)
        element_type: Type of element to replace (optional)
        material_image: Uploaded material texture (optional)
        material_id: ID of material from MATERIALS library (optional)
        method: Replacement method ("cv_poisson" or "comfyui")
        scale: Scale factor for texture
        angle_bias_deg: Angle bias for texture orientation
        color_match: Color matching method ("reinhard" or None)
        preserve_shading: Whether to preserve original shading (1=True, 0=False)
        material_prominence: Material overlay prominence (0.0-1.0, default 0.7 for 70% visibility)
    
    Returns:
        dict: Result with replaced image and metadata
    """
    try:
        t0 = time.time()

        # --- download and decode original image ---
        try:
            response = requests.get(original_image, timeout=30)
            response.raise_for_status()
            original_cv = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
            if original_cv is None:
                raise HTTPException(status_code=400, detail="Invalid original_image format")
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Failed to download original_image: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing original_image: {str(e)}")
 
        H, W = original_cv.shape[:2]

        # --- choose material texture ---
        texture_cv = None
        
        if material_image is not None:
            # Use uploaded material image
            content = material_image.read()
            texture_cv = cv2.imdecode(np.frombuffer(content, np.uint8), cv2.IMREAD_COLOR)
        elif material_id:
            # Download material image from PRODUCT_IMAGE_MAP directly to memory
            material_content = download_material_image_binary(material_id)
            texture_cv = cv2.imdecode(np.frombuffer(material_content, np.uint8), cv2.IMREAD_COLOR)
            
        if method == "cv_poisson" and texture_cv is None:
            raise HTTPException(status_code=400, detail="No material texture: provide material_image or valid material_id")

        # --- build refined mask ---
        refined_mask = None

        if element_id and elements_json:
            # Build a refined mask for a single element using the same approach
            # as the element_type path but scoped to the selected element.
            try:
                elements = json.loads(elements_json)
            except Exception:
                raise HTTPException(status_code=400, detail="elements_json must be a JSON-encoded list")

            # Locate the target element by id
            target_elem = None
            for e in elements or []:
                if str(e.get("id")).lower() == str(element_id).lower():
                    target_elem = e
                    break
            if target_elem is None:
                raise HTTPException(status_code=400, detail=f"element_id '{element_id}' not found in elements_json")

            coords = target_elem.get("coordinates")
            if not coords:
                raise HTTPException(status_code=400, detail=f"element_id '{element_id}' has no coordinates")

            target_type = (target_elem.get("type") or target_elem.get("class") or "").lower().strip()
            include_ids = {str(target_elem.get("id"))}
            include_types = {target_type} if target_type else None

            edge_margin = _calc_edge_margin_px(H, W)
            erosion = _calc_erosion_px(H, W)
            refined_mask = build_selection_mask(
                elements,
                H,
                W,
                include_ids=include_ids,
                include_types=include_types,
                exclude_types=(DEFAULT_EXCLUDE_TYPES - include_types),
                edge_margin_px=edge_margin,
                erosion_px=erosion,
                remove_other_geometry=True,
            )

            if refined_mask is None or np.count_nonzero(refined_mask) == 0:
                target_mask = _poly_to_mask(coords, H, W)
                exc = _union_mask(elements, DEFAULT_EXCLUDE_TYPES, H, W)
                k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*edge_margin+1, 2*edge_margin+1))
                exc = cv2.dilate(exc, k, 1)
                refined_mask = cv2.bitwise_and(target_mask, cv2.bitwise_not(exc))
                if erosion > 0:
                    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*erosion+1, 2*erosion+1))
                    refined_mask = cv2.erode(refined_mask, k, 1)
                refined_mask = cv2.morphologyEx(refined_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), 1)

        elif elements_json and element_type:
            try:
                elements = json.loads(elements_json)
            except Exception:
                raise HTTPException(status_code=400, detail="elements_json must be a JSON-encoded list")

            ttype = element_type.lower().strip()
            include_types = {ttype}

            exclude_types = (DEFAULT_EXCLUDE_TYPES - include_types)

            edge_margin = _calc_edge_margin_px(H, W)
            erosion = _calc_erosion_px(H, W)

            refined_mask = build_selection_mask(
                elements,
                H,
                W,
                include_types=include_types,
                exclude_types=exclude_types,
                edge_margin_px=edge_margin,
                erosion_px=erosion,
                remove_other_geometry=False,
            )

            if refined_mask is None or np.count_nonzero(refined_mask) == 0:
                refined_mask = build_refined_mask(elements, include_types, exclude_types, H, W, edge_margin_px=edge_margin)
        
        elif mask_image:
            refined_mask = cv2.imdecode(np.frombuffer(base64.b64decode(mask_image), np.uint8), cv2.IMREAD_GRAYSCALE)

        else:
            raise HTTPException(status_code=400, detail="Provide either (elements_json + element_type) or mask_image")

        if refined_mask is None or np.count_nonzero(refined_mask) == 0:
            raise HTTPException(status_code=422, detail="Refined mask is empty for the requested target")

        # --- apply cv_poisson method ---
        if method == "cv_poisson":
            # Use element-specific scale for element_id, otherwise use provided scale
            texture_scale = float(scale)
            if element_id and elements_json:
                # Calculate element-specific scale based on target element dimensions
                try:
                    elements = json.loads(elements_json)
                    target_elem = None
                    for e in elements or []:
                        if str(e.get("id")).lower() == str(element_id).lower():
                            target_elem = e
                            break
                    
                    if target_elem:
                        texture_scale = _calculate_element_specific_scale(target_elem, H, W)
                        logger.info(f"Using element-specific scale: {texture_scale:.2f} for element_id: {element_id}")
                    else:
                        logger.warning(f"Could not find element {element_id} for scale calculation, using default scale: {texture_scale}")
                except Exception as e:
                    logger.warning(f"Error calculating element-specific scale: {e}, using default scale: {texture_scale}")
            
            out = apply_texture_per_region(
                original=original_cv,
                union_mask=refined_mask,
                texture=texture_cv,
                scale=texture_scale,
                angle_mode="auto",
                angle_bias_deg=float(angle_bias_deg),
                color_match=(color_match if color_match in ["reinhard"] else None),
                preserve_shading=bool(int(preserve_shading)),
                material_prominence=float(material_prominence),
            )
            out_b64, out_size_mb, (out_w, out_h), out_downscaled = _encode_output_image(out)

            if str(response_mode).lower() == "url":
                temp_out_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_render.png")
                try:
                    # write the already-encoded image to disk
                    with open(temp_out_path, "wb") as f:
                        f.write(base64.b64decode(out_b64))

                    # folder prefix mirrors your old structure: renders[/<element_type>]
                    key_prefix = "renders"
                    if element_type:
                        key_prefix = f"{key_prefix}/{str(element_type).lower()}"

                    s3_key, s3_url = s3_upload_file(temp_out_path, key_prefix=key_prefix)

                    replaced_image_url = s3_url
                    public_id = s3_key  # keep field name; now it's the S3 object key
                    width = out_w
                    height = out_h
                    return {
                        "success": True,
                        "method": method,
                        "element_type": element_type,
                        "material_id": material_id,
                        "processing_time": f"{time.time() - t0:.2f}s",
                        "output_image_mb": round(out_size_mb, 3),
                        "output_image_dimensions": {"width": int(width), "height": int(height)},
                        "output_image_downscaled": out_downscaled,
                        "replaced_image_url": replaced_image_url,
                        "public_id": public_id,
                    }

                except Exception as e:
                    logger.error(f"Error uploading to Cloudinary: {str(e)}")
                    raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")

                # ---- default: existing base64 behavior (unchanged) ----
            return {
                "success": True,
                "method": method,
                "element_type": element_type,
                "material_id": material_id,
                "processing_time": f"{time.time() - t0:.2f}s",
                "output_image_mb": round(out_size_mb, 3),
                "output_image_dimensions": {"width": out_w, "height": out_h},
                "output_image_downscaled": out_downscaled,
                "replaced_image": out_b64,
            }
        else:
            raise HTTPException(status_code=400, detail="Only 'cv_poisson' method is supported in this service")

    except HTTPException as e:
        logger.error(f"1st exception Error in advanced_material_replacement: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"2nd exception Error in advanced_material_replacement: {str(e)}")
        raise e

