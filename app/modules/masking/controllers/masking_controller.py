from src.model_functions import model_generate_mask, model_replace_material, model_segment_image
from src.logger import logger
from fastapi import UploadFile, File, HTTPException, Form, APIRouter

masking_router = APIRouter(prefix="/masking", tags=["masking"])


@masking_router.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    try:
        return model_segment_image(file)

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@masking_router.post("/generate_mask")
async def generate_mask(
        original_image: str = Form(...),
        material_image: UploadFile = File(...),
        element_type: str = Form(...),
        coordinates: str = Form(...)
):
    try:
        return model_generate_mask(original_image, material_image, element_type, coordinates)

    except Exception as e:
        logger.error(f"Error generating mask: {str(e)}")
        return HTTPException(status_code=500, detail=str(e))


@masking_router.post("/replace_material")
async def replace_material(
        original_image: str = Form(...),
        mask_image: str = Form(...),
        material_image: UploadFile = File(...),
        element_type: str = Form(...),
        prompt: str = Form(None),
        seed: int = Form(None)
):
    try:
        return model_replace_material(original_image, mask_image, material_image, element_type, prompt, seed)
    except Exception as e:
        logger.error(f"Error replacing material for {element_type}: {str(e)}")
        return HTTPException(status_code=500, detail=str(e))