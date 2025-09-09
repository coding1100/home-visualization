import os
import time
import json
import copy
import uuid
import asyncio
import aiohttp  

import numpy as np

from src.logger import logger
from src.utils import upload_image
from src.constants import FIXED_SEED, UPLOAD_DIR
from app.core.config import settings


async def process_with_comfyui(original_path, mask_path, material_path, prompt, element_type):
    """
    Process images using ComfyUI API with the house-visualizer workflow
    
    Returns:
        tuple: (output_path, seed_value) - Path to the generated image and the seed used
    """
    try:
        start_time = time.time()
        logger.info(f"Starting ComfyUI processing for {element_type}")
        
        # Cache workflow to avoid loading it repeatedly
        global cached_workflow
        if not cached_workflow:
            # Load the workflow JSON
            workflow_path = os.path.join(os.path.dirname(__file__), "house-visualizer-with-prompt.json")
            with open(workflow_path, "r") as f:
                cached_workflow = json.load(f)
        
        # Create a copy of the workflow to modify
        workflow = copy.deepcopy(cached_workflow)
        
        # Use the configured ComfyUI server address
        comfyui_server = settings.COMFYUI_SERVER
        
        # Modify the workflow with our input images and parameters
        
        # Set the original image in the workflow (node 4)
        workflow["4"]["inputs"]["image"] = os.path.basename(original_path)
        
        # Set the material image in the workflow (node 39)
        workflow["39"]["inputs"]["image"] = os.path.basename(material_path)
        
        # Set the mask image in the workflow (node 180)
        workflow["180"]["inputs"]["image"] = os.path.basename(mask_path)
        
        # Update the prompt in the workflow (node 187/186)
        if "187" in workflow and "186" in workflow:
            # For house-visualizer-with-prompt.json
            workflow["178"]["inputs"]["text"] = element_type
        elif "182" in workflow:
            # For original house-visualizer.json
            workflow["182"]["inputs"]["text"] = prompt
        
        # Set a random seed for the SeedGenerator (node 177)
        if FIXED_SEED > 0:
            # Use the fixed seed for reproducibility
            seed_value = FIXED_SEED
            logger.info(f"Using fixed seed: {seed_value} for material replacement")
        else:
            # Generate a random seed between 0 and 2^63-1
            seed_value = np.random.randint(0, 2**63 - 1)
            logger.info(f"Using random seed: {seed_value} for material replacement")
        
        # Set the seed in the workflow
        workflow["177"]["inputs"]["seed"] = int(seed_value)
        
        # Generate a client_id
        client_id = str(uuid.uuid4())
        
        # Use asyncio for concurrent uploads
        upload_tasks = []
        upload_url = f"{comfyui_server}/upload/image"
        
        for img_path in [original_path, mask_path, material_path]:
            task = asyncio.create_task(upload_image(upload_url, img_path))
            upload_tasks.append(task)
        
        # Wait for all uploads to complete
        await asyncio.gather(*upload_tasks)
        
        # Queue the prompt
        queue_url = f"{comfyui_server}/prompt"
        queue_data = {
            "prompt": workflow,
            "client_id": client_id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(queue_url, json=queue_data) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Failed to queue prompt: {error_text}")
                
                response_data = await response.json()
                prompt_id = response_data["prompt_id"]
                logger.info(f"Queued prompt with ID: {prompt_id}")
        
        # Poll for completion
        history_url = f"{comfyui_server}/history"
        output_path = None
        max_attempts = 60  # Maximum number of attempts (10 minutes with 10-second interval)
        attempts = 0
        
        async with aiohttp.ClientSession() as session:
            while attempts < max_attempts:
                async with session.get(history_url) as response:
                    if response.status == 200:
                        history = await response.json()
                        if prompt_id in history:
                            if history[prompt_id].get("status", {}).get("completed", False):
                                # Get the output image
                                outputs = history[prompt_id].get("outputs", {})
                                if outputs:
                                    for node_id, node_output in outputs.items():
                                        if "images" in node_output:
                                            for img_data in node_output["images"]:
                                                # Download the image
                                                img_filename = img_data["filename"]
                                                img_subfolder = img_data.get("subfolder", "")
                                                img_url = f"{comfyui_server}/view?filename={img_filename}&subfolder={img_subfolder}"
                                                
                                                async with session.get(img_url) as img_response:
                                                    if img_response.status == 200:
                                                        output_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_output.png")
                                                        content = await img_response.read()
                                                        with open(output_path, "wb") as f:
                                                            f.write(content)
                                                        logger.info(f"Saved output image to {output_path}")
                                                        
                                                        end_time = time.time()
                                                        logger.info(f"ComfyUI processing completed in {end_time - start_time:.2f} seconds")
                                                        return output_path, seed_value
                                break
                
                # Wait before polling again
                await asyncio.sleep(5)  # Reduced polling interval
                attempts += 1
        
        if output_path is None:
            raise Exception("Failed to get output image from ComfyUI")
        
        return output_path, seed_value
        
    except Exception as e:
        logger.error(f"Error in ComfyUI processing: {str(e)}")
        raise
