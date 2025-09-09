import os
import aiohttp
import base64
import asyncio
import time
import random
import numpy as np
import torch

from src.logger import logger

async def upload_image(upload_url, img_path):
    """Helper function to upload images to ComfyUI"""
    filename = os.path.basename(img_path)
    
    with open(img_path, "rb") as img_file:
        data = aiohttp.FormData()
        data.add_field('image', img_file, filename=filename, content_type='image/png')
        
        async with aiohttp.ClientSession() as session:
            async with session.post(upload_url, data=data) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Failed to upload image {filename}: {error_text}")
                
                return await response.json()

async def cleanup_temp_files(file_paths):
    """Clean up temporary files after a delay to ensure they're not still in use"""
    try:
        await asyncio.sleep(60)  # Wait a minute before cleaning up
        for path in file_paths:
            if os.path.exists(path):
                os.remove(path)
                logger.debug(f"Removed temporary file: {path}")
    except Exception as e:
        logger.error(f"Error cleaning up temporary files: {str(e)}")

def image_to_base64(image_path):
    """Convert image to base64 with optimized performance"""
    try:
        # Use memory mapping for faster file reading
        with open(image_path, "rb") as img_file:
            img_data = img_file.read()
        
        # Use faster base64 encoding
        encoded = base64.b64encode(img_data)
        return encoded.decode('utf-8')
    except Exception as e:
        logger.error(f"Error in image_to_base64: {str(e)}")
        return ""

def get_color_for_class(class_name):
    # Default colors for different house elements
    color_map = {
        "roof": "#8B4513",  # Brown
        "wall": "#F5F5DC",  # Beige
        "window": "#87CEEB",  # Sky Blue
        "door": "#654321",  # Dark Brown
        "chimney": "#A52A2A",  # Brown/Red
        "foundation": "#808080",  # Gray
        # Add more as needed
    }
    return color_map.get(class_name.lower(), "#CCCCCC")  # Default gray if not found

def get_material_for_class(class_name):
    # Default materials for different house elements
    material_map = {
        "roof": "shingles",
        "wall": "brick", 
        "window": "glass",
        "door": "wood",
        "chimney": "brick",
        "foundation": "concrete",
        # Add more as needed
    }
    return material_map.get(class_name.lower(), "unknown")

def set_global_seed(seed=None):
    """
    Set the global random seed for reproducibility across all random generators
    
    Args:
        seed (int, optional): Seed value to use. If None, a random seed will be generated.
    
    Returns:
        int: The seed that was set
    """
    if seed is None or seed <= 0:
        # Generate a random seed if none provided or if it's negative/zero
        seed = int(time.time() * 1000) % (2**32 - 1)
    
    # Set seed for numpy random
    np.random.seed(seed)
    
    # Set seed for Python's random
    random.seed(seed)
    
    # Set seed for PyTorch if available
    if torch and hasattr(torch, "manual_seed"):
        torch.manual_seed(seed)
        if torch.cuda.is_available() and hasattr(torch.cuda, "manual_seed_all"):
            torch.cuda.manual_seed_all(seed)
    
    logger.info(f"Global random seed set to: {seed}")
    return seed
