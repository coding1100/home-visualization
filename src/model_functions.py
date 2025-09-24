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



def _prepare_for_cloudinary_upload(path: str, max_bytes: int = CLOUDINARY_MAX_IMAGE_BYTES) -> tuple[str, bool]:

    """

    Ensure 'path' is under Cloudinary image size cap.

    Returns (upload_path, temp_created). If temp_created is True, caller should delete it.

    """

    try:

        if os.path.getsize(path) <= max_bytes:

            return path, False



        img = cv2.imread(path)

        if img is None:

            return path, False



        h, w = img.shape[:2]

        scale = 1.0

        quality = 90

        tmp_out = None

        buf = None



        # Reduce JPEG quality first, then downscale if still too big

        for _ in range(8):

            resized = img if scale >= 0.999 else cv2.resize(img, (max(1, int(w * scale)), max(1, int(h * scale))), interpolation=cv2.INTER_AREA)

            ok, buf = cv2.imencode(".jpg", resized, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

            if not ok:

                break

            if len(buf) <= max_bytes:

                tmp_out = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_cld.jpg")

                with open(tmp_out, "wb") as f:

                    f.write(buf.tobytes())

                return tmp_out, True

            # tighten knobs

            if quality > 65:

                quality -= 10

            else:

                scale *= 0.85



        # Final attempt with whatever we have

        if buf is not None:

            tmp_out = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_cld.jpg")

            with open(tmp_out, "wb") as f:

                f.write(buf.tobytes())

            return tmp_out, True



        return path, False

    except Exception:

        # If anything fails, fall back to original path (Cloudinary may still reject it)

        return path, False

def _ensure_cloudinary_config():
    cfg = cloudinary.config()
    # If this module was imported before your app-wide config ran, fill it here.
    if not cfg.api_key or not cfg.api_secret or not cfg.cloud_name:
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True,
        )


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


# def model_segment_image(
#     file: UploadFile,
#         response_mode: str = "base64"  # NEW (optional, keeps old behavior)
# ):
#
#         # Start timing for performance measurement
#         start_time = time.time()
#
#         # Generate a unique file name
#         file_extension = file.filename.split(".")[-1]
#         file_name = f"{uuid.uuid4()}.{file_extension}"
#         file_path = os.path.join(UPLOAD_DIR, file_name)
#
#         # Save the uploaded file
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#
#         # Process the image with Roboflow model
#         result = model.predict(file_path, confidence=25).json()
#
#         # Get the labels for each detection
#         labels = [item["class"] for item in result["predictions"]]
#
#         # Create detections object from inference result
#         detections = sv.Detections.from_inference(result)
#
#         # Read the original image
#         image = cv2.imread(file_path)
#
#         # Create annotators
#         label_annotator = sv.LabelAnnotator()
#         mask_annotator = sv.MaskAnnotator()
#
#         # Annotate the image
#         annotated_image = mask_annotator.annotate(
#             scene=image, detections=detections)
#         annotated_image = label_annotator.annotate(
#             scene=annotated_image, detections=detections, labels=labels)
#
#         # Save the annotated image
#         annotated_path = os.path.join(UPLOAD_DIR, f"annotated_{file_name}")
#         cv2.imwrite(annotated_path, annotated_image)
#
#         # Convert original and annotated images to base64
#         original_base64 = image_to_base64(file_path)
#         annotated_base64 = image_to_base64(annotated_path)
#
#         # Extract house elements data for the frontend
#         house_elements = []
#         for i, pred in enumerate(result["predictions"]):
#             points = []
#             if "points" in pred:
#                 points = pred["points"]
#             elif "x" in pred and "y" in pred and "width" in pred and "height" in pred:
#                 # Convert bounding box to polygon points
#                 x, y, w, h = pred["x"], pred["y"], pred["width"], pred["height"]
#                 points = [
#                     [x - w/2, y - h/2],
#                     [x + w/2, y - h/2],
#                     [x + w/2, y + h/2],
#                     [x - w/2, y + h/2]
#                 ]
#
#             element = {
#                 "id": f"{pred['class']}-{i}",
#                 "name": f"{pred['class'].capitalize()} {i+1}",
#                 "type": pred["class"],
#                 "color": get_color_for_class(pred["class"]),
#                 "material": get_material_for_class(pred["class"]),
#                 "coordinates": points,
#                 "confidence": pred["confidence"],
#                 "originalColor": get_color_for_class(pred["class"])
#             }
#             house_elements.append(element)
#         mode = (response_mode or "base64").lower()
#         if mode == "url":
#             _ensure_cloudinary_config()  # <<< important
#
#             # Use the *same* style as your working uploader: resource_type="auto"
#             # Folder pattern matches what you used for renders (no surprises).
#             upload_folder = "renders"
#
#             try:
#                 # upload original
#                 res_orig = cloudinary.uploader.upload(
#                     file_path,
#                     folder=upload_folder,
#                     resource_type="auto",
#                     use_filename=True,
#                     unique_filename=True,
#                     overwrite=False,
#                 )
#                 # upload annotated
#                 res_anno = cloudinary.uploader.upload(
#                     annotated_path,
#                     folder=upload_folder,
#                     resource_type="auto",
#                     use_filename=True,
#                     unique_filename=True,
#                     overwrite=False,
#                 )
#                 original_url = res_orig.get("secure_url")
#                 annotated_url = res_anno.get("secure_url")
#             except Exception as e:
#                 # same error style you’re already using elsewhere
#                 raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")
#
#             end_time = time.time()
#             logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")
#
#             # optional cleanup of local temp images (safe no-op if you want to keep them)
#             # try:
#             #     os.remove(file_path)
#             #     os.remove(annotated_path)
#             # except Exception:
#             #     pass
#
#             return {
#                 "success": True,
#                 "original_image_url": original_url,
#                 "annotated_image_url": annotated_url,
#                 "house_elements": house_elements,
#                 "raw_predictions": result["predictions"],
#                 "processing_time": f"{end_time - start_time:.2f}s",
#             }
#
#         # ---- default (unchanged): base64 payloads ----
#         original_base64 = image_to_base64(file_path)
#         annotated_base64 = image_to_base64(annotated_path)
#
#         end_time = time.time()
#         logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")
#
#         return {
#             "success": True,
#             "original_image": original_base64,
#             "annotated_image": annotated_base64,
#             "house_elements": house_elements,
#             "raw_predictions": result["predictions"],
#             "processing_time": f"{end_time - start_time:.2f}s",
#         }
#
#         # end_time = time.time()
#
#
#         # logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")
#         #
#         # return {
#         #     "success": True,
#         #     "original_image": original_base64,
#         #     "annotated_image": annotated_base64,
#         #     "house_elements": house_elements,
#         #     "raw_predictions": result["predictions"],
#         #     "processing_time": f"{end_time - start_time:.2f}s"
#         # }



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
    preserve_shading: int = 1,
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
            preserve_shading=preserve_shading,
            response_mode=response_mode,

        )
    except Exception as e:
        logger.error(f"Error in advanced material replacement: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def model_segment_image(
    file: Optional[UploadFile],
    image_id: Optional[str] = None,
    db: Optional[AsyncSession] = None,
    response_mode: str = "base64",
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

    # ---------- Resolve input image (either from DB via image_id OR from uploaded file) ----------
    used_gallery = False
    source_info = None

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
                pil_img.save(file_path, format="JPEG")  # overwrite as RGB JPEG
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image preprocessing failed: {e}")
    # ---------- Roboflow inference (unchanged) ----------
    result = model.predict(file_path, confidence=25).json()
    print(f"Model Successfully Predicted:")
    labels = [item["class"] for item in result["predictions"]]
    detections = sv.Detections.from_inference(result)
    print(f"Detections Successfully Saved:")
    image = cv2.imread(file_path)
    label_annotator = sv.LabelAnnotator()
    mask_annotator = sv.MaskAnnotator()

    annotated_image = mask_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

    annotated_path = os.path.join(UPLOAD_DIR, f"annotated_{file_name}")
    cv2.imwrite(annotated_path, annotated_image)
    print(f"Annotated Image Successfully Saved:")
    # ---------- Build house elements (unchanged) ----------
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

    mode = (response_mode or "base64").lower()

    # ---------- URL mode: upload to Cloudinary (same pattern you already use) ----------
    if mode == "url":
        # Only upload the original if it *didn’t* come from gallery DB (avoid duplicate uploads)
        original_url: Optional[str] = None
        if used_gallery:
            original_url = source_info["secure_url"]
        else:
            upload_path, tmp1 = _prepare_for_cloudinary_upload(file_path)
            try:
                res_orig = cloudinary.uploader.upload(
                    upload_path,
                    folder="renders",
                    resource_type="auto",
                    use_filename=True,
                    unique_filename=True,
                    overwrite=False,
                )
                original_url = res_orig.get("secure_url")
            except Exception as e:
                raise HTTPException(status_code=502, detail=f"Cloudinary upload failed (original): {e}")
            finally:
                if tmp1:
                    os.remove(upload_path)

        upload_anno_path, tmp2 = _prepare_for_cloudinary_upload(annotated_path)
        try:
            res_anno = cloudinary.uploader.upload(
                upload_anno_path,
                folder="renders",
                resource_type="auto",
                use_filename=True,
                unique_filename=True,
                overwrite=False,
            )
            annotated_url = res_anno.get("secure_url")
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Cloudinary upload failed (annotated): {e}")
        finally:
            if tmp2:
                try: os.remove(upload_anno_path)
                except Exception: pass

        end_time = time.time()
        logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")

        resp = {
            "success": True,
            "original_image_url": original_url,
            "annotated_image_url": annotated_url,
            "house_elements": house_elements,
            "raw_predictions": result["predictions"],
            "processing_time": f"{end_time - start_time:.2f}s",
        }
        # Include source image details ONLY when image_id was used
        if used_gallery and source_info:
            resp["source_image"] = source_info
        return resp

    # ---------- Default (unchanged): base64 payloads ----------
    original_base64 = image_to_base64(file_path)
    annotated_base64 = image_to_base64(annotated_path)

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
    if used_gallery and source_info:
        resp["source_image"] = source_info
    return resp
