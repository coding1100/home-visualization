import os
import time
import uuid
import json
import base64
import numpy as np
import cv2
import requests
from typing import List, Dict, Any, Optional
from fastapi import HTTPException, UploadFile

from src.logger import logger
from src.constants import UPLOAD_DIR
from app.modules.catalog.data.product_images import PRODUCT_IMAGE_MAP

# ====== MATERIAL LIBRARY ======
MATERIALS = {
    # "id": absolute_or_relative_path_to_texture_image
    "wall_1": "materials/wall_1.jpg",
    "wall_2": "materials/wall_2.jpg",
    "garage_1": "materials/garage_1.jpg",
    "garage_2": "materials/garage_2.jpg",
    # add your catalog here…
}

# ====== GEOMETRY / MASK HELPERS ======
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
    """Tile texture with scaling and rotation."""
    Hc, Wc = canvas_hw
    h, w = tex_bgr.shape[:2]
    # scale
    new_w = max(1, int(w*scale)); new_h = max(1, int(h*scale))
    tex = cv2.resize(tex_bgr, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
    # rotate
    M = cv2.getRotationMatrix2D((new_w/2, new_h/2), angle_deg, 1.0)
    tex = cv2.warpAffine(tex, M, (new_w, new_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    # tile
    tiles_x = int(np.ceil(Wc/new_w)) + 1
    tiles_y = int(np.ceil(Hc/new_h)) + 1
    tiled = np.tile(tex, (tiles_y, tiles_x, 1))[:Hc, :Wc]
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
    pad=16, erosion_px=1, clone_mode=cv2.MIXED_CLONE
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

    # perspective-ish warp of tiled texture
    canvas_size = (max(H,W), max(H,W))
    tiled = tile_texture(texture_bgr, canvas_size, scale=scale, angle_deg=angle_deg)
    ys, xs = np.where(mask_bin>0)
    pts = np.stack([xs, ys], axis=1).astype(np.float32).reshape(-1,1,2)
    pts = cv2.approxPolyDP(pts, 2.0, True)
    rect = cv2.minAreaRect(pts)
    dst_quad = cv2.boxPoints(rect).astype(np.float32)
    src_quad = np.array([[0,0],[canvas_size[1]-1,0],[canvas_size[1]-1,canvas_size[0]-1],[0,canvas_size[0]-1]], dtype=np.float32)
    Hmat = cv2.getPerspectiveTransform(src_quad, dst_quad)
    src_warp = cv2.warpPerspective(tiled, Hmat, (W,H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

    if preserve_shading:
        lab_o = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
        lab_s = cv2.cvtColor(src_warp,     cv2.COLOR_BGR2LAB).astype(np.float32)
        L = lab_o[...,0]; a_s, b_s = lab_s[...,1], lab_s[...,2]
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

    try:
        blended_roi = cv2.seamlessClone(roi_src, roi_dst, roi_mask_u8, (cx,cy), clone_mode)
    except cv2.error:
        try:
            blended_roi = cv2.seamlessClone(roi_src, roi_dst, roi_mask_u8, (cx,cy), cv2.NORMAL_CLONE)
        except cv2.error:
            alpha = (roi_mask_u8.astype(np.float32)/255.0)[...,None]
            blended_roi = (roi_src*alpha + roi_dst*(1.0-alpha)).astype(np.uint8)

    out = original_bgr.copy()
    out[y0:y1, x0:x1] = blended_roi
    return out

def apply_texture_per_region(original, union_mask, texture, scale=1.0, angle_mode="auto",
                             angle_bias_deg=90.0, color_match=None, preserve_shading=True):
    """Clone per connected wall (stable angles, avoids cross-bleed)."""
    out = original.copy()
    cnts, _ = cv2.findContours(union_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        sub = np.zeros_like(union_mask); cv2.drawContours(sub, [c], -1, 255, -1)
        a = _auto_angle_from_cnt(c) if angle_mode=="auto" else float(angle_mode)
        a = float(a) + float(angle_bias_deg)
        out = apply_texture_cv_poisson(out, sub, texture, scale=scale, angle_deg=a,
                                       color_match=color_match, preserve_shading=preserve_shading)
    return out

def save_tmp_png(bgr_img):
    """Helper to save a tmp PNG and return its path for base64 encoding."""
    out_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_out.png")
    cv2.imwrite(out_path, bgr_img, [cv2.IMWRITE_PNG_COMPRESSION, 1])
    return out_path

def download_material_image(material_id: str) -> str:
    """
    Download material image from URL and return temporary file path.
    
    Args:
        material_id: Material ID from PRODUCT_IMAGE_MAP
        
    Returns:
        str: Path to downloaded temporary material image
        
    Raises:
        HTTPException: If material_id not found or download fails
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
        # Create tmp directory if it doesn't exist
        tmp_dir = os.path.join(UPLOAD_DIR, "tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        
        # Generate temporary filename
        file_extension = image_url.split('.')[-1].split('?')[0]  # Handle URLs with query params
        if file_extension not in ['jpg', 'jpeg', 'png', 'webp']:
            file_extension = 'jpg'  # Default fallback
        
        temp_filename = f"{uuid.uuid4()}_material.{file_extension}"
        temp_path = os.path.join(tmp_dir, temp_filename)
        
        # Download the image
        logger.info(f"Downloading material image from: {image_url}")
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Save to temporary file
        with open(temp_path, 'wb') as f:
            f.write(response.content)
        
        logger.info(f"Material image downloaded to: {temp_path}")
        return temp_path
        
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
    material_image: Optional[UploadFile] = None,
    material_id: Optional[str] = None,
    method: str = "cv_poisson",
    scale: float = 1.0,
    angle_bias_deg: float = 90.0,
    color_match: Optional[str] = None,
    preserve_shading: int = 1
):
    """
    Advanced material replacement with cv_poisson method.
    
    Args:
        original_image: Base64 encoded original image
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
    
    Returns:
        dict: Result with replaced image and metadata
    """
    try:
        t0 = time.time()

        # --- decode original image ---
        original_cv = cv2.imdecode(np.frombuffer(base64.b64decode(original_image), np.uint8), cv2.IMREAD_COLOR)
        if original_cv is None:
            raise HTTPException(status_code=400, detail="Invalid original_image")
        H, W = original_cv.shape[:2]

        # --- choose material texture ---
        texture_cv = None
        temp_material_path = None
        
        if material_image is not None:
            # Use uploaded material image
            content = material_image.read()
            texture_cv = cv2.imdecode(np.frombuffer(content, np.uint8), cv2.IMREAD_COLOR)
        elif material_id:
            # Download material image from PRODUCT_IMAGE_MAP
            temp_material_path = download_material_image(material_id)
            texture_cv = cv2.imread(temp_material_path, cv2.IMREAD_COLOR)
            
        if method == "cv_poisson" and texture_cv is None:
            raise HTTPException(status_code=400, detail="No material texture: provide material_image or valid material_id")

        # --- build refined mask ---
        refined_mask = None

        if elements_json and element_type:
            try:
                elements = json.loads(elements_json)
            except Exception:
                raise HTTPException(status_code=400, detail="elements_json must be a JSON-encoded list")

            ttype = element_type.lower().strip()
            include_types = {ttype}

            # default excludes so target never overlaps other facade parts
            default_excludes = {"window","door","garage","garage door","frame","trim","pillar","column","stone","foundation","fence","shutter","railing"}
            exclude_types = default_excludes - include_types

            refined_mask = build_refined_mask(elements, include_types, exclude_types, H, W, edge_margin_px=2)

        elif mask_image:
            refined_mask = cv2.imdecode(np.frombuffer(base64.b64decode(mask_image), np.uint8), cv2.IMREAD_GRAYSCALE)

        else:
            raise HTTPException(status_code=400, detail="Provide either (elements_json + element_type) or mask_image")

        if refined_mask is None or np.count_nonzero(refined_mask) == 0:
            raise HTTPException(status_code=422, detail="Refined mask is empty for the requested element_type")

        # --- apply cv_poisson method ---
        if method == "cv_poisson":
            out = apply_texture_per_region(
                original=original_cv,
                union_mask=refined_mask,
                texture=texture_cv,
                scale=float(scale),
                angle_mode="auto",
                angle_bias_deg=float(angle_bias_deg),
                color_match=(color_match if color_match in ["reinhard"] else None),
                preserve_shading=bool(int(preserve_shading)),
            )
            out_b64 = base64.b64encode(cv2.imencode('.png', out)[1]).decode('utf-8')
            
            # Clean up temporary material file if it was downloaded
            if temp_material_path and os.path.exists(temp_material_path):
                try:
                    os.remove(temp_material_path)
                    logger.info(f"Cleaned up temporary material file: {temp_material_path}")
                except Exception as e:
                    logger.warning(f"Failed to clean up temporary material file {temp_material_path}: {str(e)}")
            
            return {
                "success": True,
                "method": method,
                "element_type": element_type,
                "material_id": material_id,
                "processing_time": f"{time.time()-t0:.2f}s",
                "replaced_image": out_b64
            }
        else:
            raise HTTPException(status_code=400, detail="Only 'cv_poisson' method is supported in this service")

    except HTTPException:
        # Clean up temporary material file if it was downloaded
        if 'temp_material_path' in locals() and temp_material_path and os.path.exists(temp_material_path):
            try:
                os.remove(temp_material_path)
                logger.info(f"Cleaned up temporary material file after error: {temp_material_path}")
            except Exception as cleanup_e:
                logger.warning(f"Failed to clean up temporary material file {temp_material_path}: {str(cleanup_e)}")
        raise
    except Exception as e:
        # Clean up temporary material file if it was downloaded
        if 'temp_material_path' in locals() and temp_material_path and os.path.exists(temp_material_path):
            try:
                os.remove(temp_material_path)
                logger.info(f"Cleaned up temporary material file after error: {temp_material_path}")
            except Exception as cleanup_e:
                logger.warning(f"Failed to clean up temporary material file {temp_material_path}: {str(cleanup_e)}")
        logger.exception("advanced_material_replacement failed")
        raise HTTPException(status_code=500, detail=str(e))
