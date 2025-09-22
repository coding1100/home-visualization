import time
import uuid
import os
import base64
import json

import torch
import numpy as np
import cv2
from PIL import Image
import supervision as sv
from fastapi import HTTPException, UploadFile

from src. constants import UPLOAD_DIR
from src.comfyUI import process_with_comfyui
from src.roboflow_model import model
from src.logger import logger
from src.cloudinary_func import ensure_cloudinary_config, upload_image_to_cloudinary
from src.utils import (
    get_color_for_class,
    get_material_for_class,
    set_global_seed
)
from src.material_service import advanced_material_replacement


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
    
    # Convert mask directly to base64 without saving to file
    success, buffer = cv2.imencode('.png', mask, [cv2.IMWRITE_PNG_COMPRESSION, 1])
    if not success:
        raise HTTPException(status_code=500, detail="Failed to encode mask image")
    mask_base64 = base64.b64encode(buffer.tobytes()).decode('utf-8')
    
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
        
        # Convert images to base64 for ComfyUI processing (no temp files)
        success_orig, buffer_orig = cv2.imencode('.png', original_cv, [cv2.IMWRITE_PNG_COMPRESSION, 1])
        success_mask, buffer_mask = cv2.imencode('.png', mask_cv, [cv2.IMWRITE_PNG_COMPRESSION, 1])
        success_mat, buffer_mat = cv2.imencode('.png', material_cv, [cv2.IMWRITE_PNG_COMPRESSION, 1])
        
        if not all([success_orig, success_mask, success_mat]):
            raise HTTPException(status_code=500, detail="Failed to encode images for ComfyUI processing")
        
        original_base64 = base64.b64encode(buffer_orig.tobytes()).decode('utf-8')
        mask_base64 = base64.b64encode(buffer_mask.tobytes()).decode('utf-8')
        material_base64 = base64.b64encode(buffer_mat.tobytes()).decode('utf-8')
        
        # Use ComfyUI API to process the images directly from base64
        try:
            output_base64, seed_value = process_with_comfyui(
                original_base64=original_base64,
                mask_base64=mask_base64,
                material_base64=material_base64,
                prompt=prompt,
                element_type=element_type
            )
            
            # Log performance metrics
            end_time = time.time()
            logger.info(f"Total material replacement for {element_type} completed in {end_time - start_time:.2f} seconds")
            
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


def model_segment_image(
    file: UploadFile,
        response_mode: str = "base64"  # NEW (optional, keeps old behavior)
):

        # Start timing for performance measurement
        start_time = time.time()
        
        # Read uploaded file content directly
        file_content = file.file.read()
        
        # Convert to numpy array for processing
        nparr = np.frombuffer(file_content, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Save temporarily only for Roboflow model (it requires file path)
        file_extension = file.filename.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        
        # Save temporarily for Roboflow processing
        cv2.imwrite(file_path, image)
        
        # Process the image with Roboflow model
        result = model.predict(file_path, confidence=25).json()
        
        # Clean up temp file immediately after Roboflow processing
        try:
            os.remove(file_path)
        except Exception:
            pass
        
        # Get the labels for each detection
        labels = [item["class"] for item in result["predictions"]]
        
        # Create detections object from inference result
        detections = sv.Detections.from_inference(result)
        
        # Create annotators
        label_annotator = sv.LabelAnnotator()
        mask_annotator = sv.MaskAnnotator()
        
        # Annotate the image
        annotated_image = mask_annotator.annotate(
            scene=image, detections=detections)
        annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections, labels=labels)
        
        # Convert images directly to base64 without saving to files
        success_orig, buffer_orig = cv2.imencode('.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 1])
        success_anno, buffer_anno = cv2.imencode('.png', annotated_image, [cv2.IMWRITE_PNG_COMPRESSION, 1])
        
        if not all([success_orig, success_anno]):
            raise HTTPException(status_code=500, detail="Failed to encode images")
        
        original_base64 = base64.b64encode(buffer_orig.tobytes()).decode('utf-8')
        annotated_base64 = base64.b64encode(buffer_anno.tobytes()).decode('utf-8')
        
        # Extract house elements data for the frontend
        house_elements = []
        for i, pred in enumerate(result["predictions"]):
            points = []
            if "points" in pred:
                points = pred["points"]
            elif "x" in pred and "y" in pred and "width" in pred and "height" in pred:
                # Convert bounding box to polygon points
                x, y, w, h = pred["x"], pred["y"], pred["width"], pred["height"]
                points = [
                    [x - w/2, y - h/2], 
                    [x + w/2, y - h/2], 
                    [x + w/2, y + h/2], 
                    [x - w/2, y + h/2]
                ]
            
            element = {
                "id": f"{pred['class']}-{i}",
                "name": f"{pred['class'].capitalize()} {i+1}",
                "type": pred["class"],
                "color": get_color_for_class(pred["class"]),
                "material": get_material_for_class(pred["class"]),
                "coordinates": points,
                "confidence": pred["confidence"],
                "originalColor": get_color_for_class(pred["class"])
            }
            house_elements.append(element)
        mode = (response_mode or "base64").lower()
        if mode == "url":
            ensure_cloudinary_config()  # <<< important
            try:
                # Convert base64 to binary for direct upload
                original_binary = base64.b64decode(original_base64)
                annotated_binary = base64.b64decode(annotated_base64)
                
                # upload original
                res_orig = upload_image_to_cloudinary(original_binary)
                # upload annotated
                res_anno = upload_image_to_cloudinary(annotated_binary)
                original_url = res_orig.get("secure_url")
                annotated_url = res_anno.get("secure_url")
            except Exception as e:
                # same error style you're already using elsewhere
                raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")

            end_time = time.time()
            logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")

            return {
                "success": True,
                "original_image_url": original_url,
                "annotated_image_url": annotated_url,
                "house_elements": house_elements,
                "raw_predictions": result["predictions"],
                "processing_time": f"{end_time - start_time:.2f}s",
            }

        # ---- default: base64 payloads (already computed above) ----

        end_time = time.time()
        logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")

        return {
            "success": True,
            "original_image": original_base64,
            "annotated_image": annotated_base64,
            "house_elements": house_elements,
            "raw_predictions": result["predictions"],
            "processing_time": f"{end_time - start_time:.2f}s",
        }

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