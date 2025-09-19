import time
import uuid
import os
import shutil
import base64
import asyncio
import json
import cloudinary, cloudinary.uploader

import torch
import numpy as np
import cv2
from PIL import Image
import supervision as sv
from fastapi import HTTPException, UploadFile

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


def model_segment_image(
    file: UploadFile,
        response_mode: str = "base64"  # NEW (optional, keeps old behavior)
):

        # Start timing for performance measurement
        start_time = time.time()
        
        # Generate a unique file name
        file_extension = file.filename.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process the image with Roboflow model
        result = model.predict(file_path, confidence=25).json()
        
        # Get the labels for each detection
        labels = [item["class"] for item in result["predictions"]]
        
        # Create detections object from inference result
        detections = sv.Detections.from_inference(result)
        
        # Read the original image
        image = cv2.imread(file_path)
        
        # Create annotators
        label_annotator = sv.LabelAnnotator()
        mask_annotator = sv.MaskAnnotator()
        
        # Annotate the image
        annotated_image = mask_annotator.annotate(
            scene=image, detections=detections)
        annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections, labels=labels)
        
        # Save the annotated image
        annotated_path = os.path.join(UPLOAD_DIR, f"annotated_{file_name}")
        cv2.imwrite(annotated_path, annotated_image)
        
        # Convert original and annotated images to base64
        original_base64 = image_to_base64(file_path)
        annotated_base64 = image_to_base64(annotated_path)
        
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
            try:
                # upload ORIGINAL
                res_orig = cloudinary.uploader.upload(
                    file_path,
                    folder="segments/originals",
                    resource_type="image",
                    use_filename=True,
                    unique_filename=True,
                    overwrite=False,
                )
                # upload ANNOTATED
                res_anno = cloudinary.uploader.upload(
                    annotated_path,
                    folder="segments/annotated",
                    resource_type="image",
                    use_filename=True,
                    unique_filename=True,
                    overwrite=False,
                )
                original_url = res_orig.get("secure_url")
                annotated_url = res_anno.get("secure_url")
            except Exception as e:
                # same error style you’re already using elsewhere
                raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")

            end_time = time.time()
            logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")

            # optional cleanup of local temp images (safe no-op if you want to keep them)
            # try:
            #     os.remove(file_path)
            #     os.remove(annotated_path)
            # except Exception:
            #     pass

            return {
                "success": True,
                "original_image_url": original_url,
                "annotated_image_url": annotated_url,
                "house_elements": house_elements,
                "raw_predictions": result["predictions"],
                "processing_time": f"{end_time - start_time:.2f}s",
            }

        # ---- default (unchanged): base64 payloads ----
        original_base64 = image_to_base64(file_path)
        annotated_base64 = image_to_base64(annotated_path)

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
        
        # end_time = time.time()


        # logger.info(f"Segmentation completed in {end_time - start_time:.2f} seconds")
        #
        # return {
        #     "success": True,
        #     "original_image": original_base64,
        #     "annotated_image": annotated_base64,
        #     "house_elements": house_elements,
        #     "raw_predictions": result["predictions"],
        #     "processing_time": f"{end_time - start_time:.2f}s"
        # }

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