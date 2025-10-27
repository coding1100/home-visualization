import time
import urllib
import uuid
import os
import shutil
import base64
import asyncio
import json
from typing import Optional

import cloudinary, cloudinary.uploader
from io import BytesIO
import torch
import numpy as np
import cv2
from PIL import Image
import supervision as sv
from fastapi import HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.modules.files.models.gallery_images import GalleryImage
from app.modules.files.s3utils.s3_utils import s3_upload_file
from app.modules.history.services.history_service import HistoryService
from src.constants import UPLOAD_DIR
from src.comfyUI import process_with_comfyui
from src.roboflow_model import model
from src.logger import logger
from src.utils import (
    image_to_base64,
    get_color_for_class,
    get_material_for_class,
    set_global_seed,
    cleanup_temp_files
)
from src.material_service import advanced_material_replacement

# Cloudinary image cap (10 MB on your account right now)

CLOUDINARY_MAX_IMAGE_BYTES = 30 * 1024 * 1024

def _jpeg_bytes_for_quality(img: Image.Image, quality: int) -> bytes:
    buf = BytesIO()
    # strip metadata by not passing exif/icc; keep resolution; compress hard
    img.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
    return buf.getvalue()

def _compress_to_target_jpeg(src_path: str, dst_path: str, target_bytes: int, min_q: int = 20, max_q: int = 95) -> int:
    """
    Binary-search JPEG quality to fit under target_bytes (same resolution).
    If even min_q can't get under target, we still return the smallest we got.
    """
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        lo, hi = min_q, max_q
        best_bytes = None
        best_len = 1 << 60
        while lo <= hi:
            q = (lo + hi) // 2
            data = _jpeg_bytes_for_quality(im, q)
            n = len(data)
            if n < best_len:
                best_bytes, best_len = data, n
            if n <= target_bytes:
                lo = q + 1
            else:
                hi = q - 1

    with open(dst_path, "wb") as f:
        f.write(best_bytes)
    return best_len


def model_generate_mask(
    original_image: str ,
    material_image,
    element_type: str,
    coordinates: str 
):
    # Start timing for performance measurement
    start_time = time.time()
    
    # Decode base64 image
    image_data = base64.b64decode(original_image)
    
    # Use numpy for faster image loading
    nparr = np.frombuffer(image_data, np.uint8)
    original_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Get image dimensions
    height, width = original_cv.shape[:2]
    
    # Create a blank mask image (black background)
    mask = np.zeros((height, width), dtype=np.uint8)
    
    # Parse coordinates
    all_coordinates = json.loads(coordinates)
    
    # Use GPU if available for polygon filling
    if torch.cuda.is_available() and len(all_coordinates) > 10:
        logger.info("Using GPU acceleration for mask generation")
        # Convert mask to tensor
        mask_tensor = torch.zeros((height, width), dtype=torch.uint8)
        if torch.cuda.is_available():
            mask_tensor = mask_tensor.cuda()
        
        # Process coordinates in batches for better GPU utilization
        for coords_set in all_coordinates:
            if not coords_set or len(coords_set) < 3:
                continue
            
            points = []
            for coord in coords_set:
                if isinstance(coord, list) and len(coord) >= 2:
                    points.append([int(coord[0]), int(coord[1])])
                elif isinstance(coord, dict) and 'x' in coord and 'y' in coord:
                    points.append([int(coord['x']), int(coord['y'])])
            
            if len(points) < 3:
                continue
            
            # Convert to numpy array for OpenCV
            points_np = np.array(points, dtype=np.int32)
            points_np = points_np.reshape((-1, 1, 2))
            
            # Use OpenCV for polygon filling (still faster for individual polygons)
            cv2.fillPoly(mask, [points_np], 255)
    else:
        # Use OpenCV for CPU processing (still very efficient)
        for coords_set in all_coordinates:
            # Convert coordinates to numpy array of points
            if not coords_set or len(coords_set) < 3:
                continue
                
            points = []
            for coord in coords_set:
                if isinstance(coord, list) and len(coord) >= 2:
                    points.append([int(coord[0]), int(coord[1])])
                elif isinstance(coord, dict) and 'x' in coord and 'y' in coord:
                    points.append([int(coord['x']), int(coord['y'])])
            
            if len(points) < 3:
                continue
                
            # Convert to numpy array and reshape for fillPoly
            points_np = np.array(points, dtype=np.int32)
            points_np = points_np.reshape((-1, 1, 2))
            
            # Fill the polygon with white color (255)
            cv2.fillPoly(mask, [points_np], 255)
    
    # Apply fast Gaussian blur for smoother edges
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    
    # Save the mask image with optimized compression
    mask_filename = f"{uuid.uuid4()}_mask.png"
    mask_path = os.path.join(UPLOAD_DIR, mask_filename)
    
    # Use optimized PNG encoding parameters
    compression_params = [cv2.IMWRITE_PNG_COMPRESSION, 1]  # Faster compression
    cv2.imwrite(mask_path, mask, compression_params)
    
    # Convert mask to base64
    mask_base64 = image_to_base64(mask_path)
    
    # Log performance metrics
    end_time = time.time()
    logger.info(f"Mask generation completed in {end_time - start_time:.2f} seconds")
    
    return {
        "success": True,
        "mask_image": mask_base64,
        "element_type": element_type,
        "processing_time": f"{end_time - start_time:.2f}s"
    }

def model_replace_material(
    original_image: str ,
    mask_image: str ,
    material_image :UploadFile,
    element_type: str ,
    prompt: str ,
    seed: int
):

        start_time = time.time()
        
        # If a seed is provided, use it to set the global seed
        if seed is not None and seed > 0:
            set_global_seed(seed)
            logger.info(f"Using user-provided seed: {seed}")
        
        # Decode base64 images directly to numpy arrays for better performance
        original_data = base64.b64decode(original_image)
        mask_data = base64.b64decode(mask_image)
        
        # Use numpy for faster image loading
        original_nparr = np.frombuffer(original_data, np.uint8)
        original_cv = cv2.imdecode(original_nparr, cv2.IMREAD_COLOR)
        
        mask_nparr = np.frombuffer(mask_data, np.uint8)
        mask_cv = cv2.imdecode(mask_nparr, cv2.IMREAD_GRAYSCALE)
        
        # Convert to PIL Images only when needed
        original_img = Image.fromarray(cv2.cvtColor(original_cv, cv2.COLOR_BGR2RGB))
        mask_img = Image.fromarray(mask_cv)
        
        # Read material image efficiently
        material_content =  material_image.read()
        material_nparr = np.frombuffer(material_content, np.uint8)
        material_cv = cv2.imdecode(material_nparr, cv2.IMREAD_COLOR)
        material_img = Image.fromarray(cv2.cvtColor(material_cv, cv2.COLOR_BGR2RGB))
        
        # Create a prompt based on the element type and material
        if not prompt:
            material_name = material_image.filename.split('.')[0]
            prompt = f"High quality {element_type} with {material_name} texture, photorealistic, detailed"
        
        logger.info(f"Processing material replacement for element type: {element_type}")
        
        # Save images for ComfyUI processing with optimized compression
        original_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_original.png")
        mask_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_mask.png")
        material_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_material.png")
        
        # Use optimized saving
        compression_params = [cv2.IMWRITE_PNG_COMPRESSION, 1]  # Faster compression
        cv2.imwrite(original_path, original_cv, compression_params)
        cv2.imwrite(mask_path, mask_cv, compression_params)
        cv2.imwrite(material_path, material_cv, compression_params)
        
        # Use ComfyUI API to process the images
        try:
            output_path, seed_value =  process_with_comfyui(
                original_path=original_path,
                mask_path=mask_path,
                material_path=material_path,
                prompt=prompt,
                element_type=element_type
            )
            
            # Convert output to base64
            output_base64 = image_to_base64(output_path)
            
            # Log performance metrics
            end_time = time.time()
            logger.info(f"Total material replacement for {element_type} completed in {end_time - start_time:.2f} seconds")
            
            # Clean up temporary files in background
            asyncio.create_task(cleanup_temp_files([original_path, mask_path, material_path, output_path]))
            
            return {
                "success": True,
                "replaced_image": output_base64,
                "element_type": element_type,
                "prompt_used": prompt,
                "processing_time": f"{end_time - start_time:.2f}s",
                "seed": seed_value
            }
            
        except Exception as comfy_error:
            logger.error(f"ComfyUI processing error for {element_type}: {str(comfy_error)}")
            raise Exception(f"Failed to process {element_type} with ComfyUI: {str(comfy_error)}")

def model_advanced_replace_material(
    original_image: str,
    mask_image: str = None,
    elements_json: str = None,
    element_type: str = None,
    element_id: str = None,
    material_image: UploadFile = None,
    material_id: str = None,
    method: str = "cv_poisson",
    scale: float = 1.0,
    angle_bias_deg: float = 90.0,
    color_match: str = None,
    orientation_mode: str = "auto",
    fixed_angle: float = 0.0,
    response_mode: str = "base64"
):
    """
    Advanced material replacement with cv_poisson method.
    Supports both mask-based and element-based replacement.
    """
    try:
        return advanced_material_replacement(
            original_image=original_image,
            mask_image=mask_image,
            elements_json=elements_json,
            element_type=element_type,
            element_id=element_id,
            material_image=material_image,
            material_id=material_id,
            method=method,
            scale=scale,
            angle_bias_deg=angle_bias_deg,
            color_match=color_match,
            orientation_mode=orientation_mode,
            fixed_angle=fixed_angle,
            response_mode=response_mode,

        )
    except Exception as e:
        logger.error(f"model func Error in advanced material replacement: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def model_segment_image(
    file: Optional[UploadFile],
    image_id: Optional[str] = None,
    db: Optional[AsyncSession] = None,
    response_mode: str = "base64",
    session_id: Optional[str] = None,
):
    """
    When image_id is provided:
      - Fetch the already-uploaded image (gallery_images) and use it as the input.
      - Add source image details to the response under 'source_image'.
    When image_id is not provided:
      - Use the uploaded file exactly like before.
    Response behavior:
      - response_mode == "url": upload original & annotated to Cloudinary (original_url comes from DB if image_id was used)
      - response_mode == "base64": same as before (original_image & annotated_image base64)
    """
    start_time = time.time()

        # threshold/target for Roboflow
    THRESHOLD_BYTES = int(9.5 * 1024 * 1024)  # if > 9.5MB -> compress
    TARGET_BYTES = int(8.5 * 1024 * 1024)  # compress to <= ~9MB
    MAX_SIDE = 4096  # longest side cap
    MAX_MP = 16_000_000  # ~16 MP cap

    # ---------- Resolve input image (either from DB via image_id OR from uploaded file) ----------
    used_gallery = False
    source_info = None
    tmp_paths: list[str] = []  # temp files to clean up
    path_for_inference: str

    if image_id:
        if db is None:
            raise HTTPException(status_code=400, detail="DB session is required when image_id is provided")

        # Look up the gallery image (id can be UUID or string)
        res = await db.execute(select(GalleryImage).where(GalleryImage.id == image_id))
        gi = res.scalar_one_or_none()
        if gi is None:
            raise HTTPException(status_code=404, detail=f"Gallery image not found for id: {image_id}")

        # Prefer secure_url, fallback to url if your model uses that field name
        src_url = getattr(gi, "secure_url", None) or getattr(gi, "url", None)
        if not src_url:
            raise HTTPException(status_code=500, detail="Gallery image record has no URL")

        # Download the image to local path (so the rest of the pipeline stays unchanged)
        # Derive name from DB or URL; fallback to a UUID-based name
        file_ext = os.path.splitext(src_url.split("?")[0].split("#")[0])[-1] or ".jpg"
        file_name = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        try:
            with urllib.request.urlopen(src_url) as r, open(file_path, "wb") as out:
                shutil.copyfileobj(r, out)
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Failed to download source image: {e}")

        used_gallery = True
        source_info = {
            "image_id": str(getattr(gi, "id", image_id)),
            "name": getattr(gi, "name", None),
            "public_id": getattr(gi, "public_id", None),
            "secure_url": src_url,
        }

    else:
        # Original behavior: save the uploaded file locally (unchanged)
        if file is None:
            raise HTTPException(status_code=400, detail="Form-data part 'file' is required")
        file_extension = file.filename.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"File Successfully Saved:")
    try:
        with Image.open(file_path) as pil_img:
            if pil_img.mode == "RGBA":
                pil_img = pil_img.convert("RGB")

                # if current path doesn't end with jpg/jpeg, rewrite to a .jpg path
                base, ext = os.path.splitext(file_path)
                new_path = base + ".jpg" if ext.lower() not in [".jpg", ".jpeg"] else file_path

                pil_img.save(new_path, format="JPEG", quality=95, optimize=True, progressive=True)

                if new_path != file_path:
                    #remove old file if we changed the extension
                    try:
                        os.remove(file_path)
                    except Exception:
                        pass
                file_path = new_path
                file_name = os.path.basename(file_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image preprocessing failed: {e}")


        # Start with original local file
    path_for_inference = file_path

    # (1) downscale if giant resolution
    try:
        with Image.open(file_path) as im_dim:
            im_dim = im_dim.convert("RGB")
            w, h = im_dim.size
            mp = w * h
            if (max(w, h) > MAX_SIDE) or (mp > MAX_MP):
                import math
                scale_side = MAX_SIDE / max(w, h)
                scale_mp = math.sqrt(MAX_MP / mp)
                scale = min(scale_side, scale_mp, 1.0)
                new_w = max(1, int(w * scale))
                new_h = max(1, int(h * scale))
                resized = im_dim.resize((new_w, new_h), Image.LANCZOS)
                base, _ = os.path.splitext(file_path)
                resized_path = base + "_resized.jpg"
                resized.save(resized_path, format="JPEG", quality=90, optimize=True, progressive=True)
                path_for_inference = resized_path
                tmp_paths.append(resized_path)
    except Exception:
        path_for_inference = file_path  # safe fallback

    # (2) compress if still > 9.5MB
    try:
        size_on_disk = os.path.getsize(path_for_inference)
    except Exception:
        size_on_disk = 0

    if size_on_disk > THRESHOLD_BYTES:
        base, _ = os.path.splitext(path_for_inference)
        infer_path = base + "_infer.jpg"
        try:
            final_len = _compress_to_target_jpeg(path_for_inference, infer_path, TARGET_BYTES, min_q=15, max_q=95)
            if final_len > TARGET_BYTES:
                _ = _compress_to_target_jpeg(path_for_inference, infer_path, int(8.0 * 1024 * 1024), min_q=10,
                                                     max_q=90)
            path_for_inference = infer_path
            tmp_paths.append(infer_path)
        except Exception:
            # if compression fails, just use whatever we had
            pass

    # ---------- Roboflow inference (unchanged) ----------
    # result = model.predict(file_path, confidence=25).json()
    result = model.predict(path_for_inference, confidence=25).json()

    print(f"Model Successfully Predicted:")
    labels = [item["class"] for item in result["predictions"]]
    detections = sv.Detections.from_inference(result)
    print(f"Detections Successfully Saved:")
    scene = cv2.imread(path_for_inference)

    # image = cv2.imread(file_path)
    label_annotator = sv.LabelAnnotator()
    mask_annotator = sv.MaskAnnotator()
    # annotated_image = mask_annotator.annotate(scene=image, detections=detections)
    annotated_image = mask_annotator.annotate(scene=scene, detections=detections)

    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

    annotated_path = os.path.join(UPLOAD_DIR, f"annotated_{file_name}")
    cv2.imwrite(annotated_path, annotated_image)
    print(f"Annotated Image Successfully Saved:")
    # ---------- Build house elements (unchanged) ----------
    house_elements_start_time = time.time()
    house_elements = []
    for i, pred in enumerate(result["predictions"]):
        points = []
        if "points" in pred:
            points = pred["points"]
        elif "x" in pred and "y" in pred and "width" in pred and "height" in pred:
            x, y, w, h = pred["x"], pred["y"], pred["width"], pred["height"]
            points = [
                [x - w / 2, y - h / 2],
                [x + w / 2, y - h / 2],
                [x + w / 2, y + h / 2],
                [x - w / 2, y + h / 2],
            ]

        element = {
            "id": f"{pred['class']}-{i}",
            "name": f"{pred['class'].capitalize()} {i + 1}",
            "type": pred["class"],
            "color": get_color_for_class(pred["class"]),
            "material": get_material_for_class(pred["class"]),
            "coordinates": points,
            "confidence": pred["confidence"],
            "originalColor": get_color_for_class(pred["class"]),
        }
        house_elements.append(element)
    house_elements_end_time = time.time()
    logger.info(f"House elements extraction completed in {house_elements_end_time - house_elements_start_time:.2f} seconds")
    print(f"House elements extraction completed in {house_elements_end_time - house_elements_start_time :.2f} seconds")

    mode = (response_mode or "base64").lower()

    # ---------- URL mode: upload to Cloudinary (same pattern you already use) ----------
    mode_uploading_start_time = time.time()
    if mode == "url":
        # Only upload the original if it *didn’t* come from gallery DB (avoid duplicate uploads)
        original_url: Optional[str] = None
        inference_url: Optional[str] = None

        if used_gallery:
            original_url = source_info["secure_url"]
        else:
            try:
                _key_o, original_url = s3_upload_file(file_path, key_prefix="renders")
            except Exception as e:
                raise HTTPException(status_code=502, detail=f"S3 upload failed (original): {e}")
        # inference: upload only if different path
        if path_for_inference != file_path:
            try:
                _key_p, inference_url = s3_upload_file(path_for_inference, key_prefix="renders")
            except Exception:
                # do not fail the whole call if this optional upload has an issue
                inference_url = None
        else:
            inference_url = original_url

            # Always upload the annotated image (it’s newly generated)
        try:
            _key_a, annotated_url = s3_upload_file(annotated_path, key_prefix="renders")
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"S3 upload failed (annotated): {e}")

        # cleanup compressed copy if we created one
        if path_for_inference != file_path:
            try:
                os.remove(path_for_inference)
            except Exception:
                pass

        end_time = time.time()
        logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")
        # This is what FE should render (compressed/inference if it exists, else original)

        original_url_for_response = inference_url or original_url

        resp = {
            "success": True,
            "original_image_url": original_url_for_response,
            "annotated_image_url": annotated_url,
            "house_elements": house_elements,
            "raw_predictions": result["predictions"],
            "processing_time": f"{end_time - start_time:.2f}s",
        }

        # ---- History logging (safe/optional; won’t break the API) ----
        try:

            base_img_id = None
            if used_gallery and source_info and source_info.get("image_id"):
                try:
                    base_img_id = uuid.UUID(str(source_info["image_id"]))
                except Exception:
                    base_img_id = None

            # base image URL the FE is actually using
            base_img_url = original_url_for_response

            if db is not None:
                await HistoryService(db).record_event(
                    session_id=session_id,  # pass session header if you capture it here
                    user_id=None,  # or user id if available
                    base_image_id=base_img_id,
                    base_image_url=base_img_url,
                    tool="segment",
                    result_url=original_url_for_response,
                    annotated_url=annotated_url,
                    params={"response_mode": "url"},
                )
        except Exception:
            # never fail the API because history logging failed
            pass
        mode_uploading_end_time = time.time()
        logger.info(f"Post-processing for URL mode completed in {mode_uploading_end_time - mode_uploading_start_time:.2f} seconds")
        print(f"Post-processing for URL mode completed in {mode_uploading_end_time - mode_uploading_start_time:.2f} seconds")
         # Clean up temp files
        if used_gallery and source_info:
            resp["source_image"] = source_info
        return resp


    start_time_3 = time.time()
    # ---------- Default (unchanged): base64 payloads ----------
    original_base64 = image_to_base64(file_path)
    annotated_base64 = image_to_base64(annotated_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(annotated_path):
        os.remove(annotated_path)
    end_time = time.time()
    logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")

    resp = {
        "success": True,
        "original_image": original_base64,
        "annotated_image": annotated_base64,
        "house_elements": house_elements,
        "raw_predictions": result["predictions"],
        "processing_time": f"{end_time - start_time:.2f}s",
    }
    end_time_3 = time.time()
    logger.info(f"Post-processing for base-64 completed in {end_time_3 - start_time_3:.2f} seconds")
    print(f"Post-processing for base-64 completed in {end_time_3 - start_time_3:.2f} seconds")
    if used_gallery and source_info:
        resp["source_image"] = source_info
    return resp
