from src.model_functions import model_generate_mask, model_replace_material, model_segment_image, model_advanced_replace_material
from src.logger import logger
from fastapi import UploadFile, File, HTTPException, Form, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.deps import get_db
masking_router = APIRouter(prefix="/masking", tags=["masking"])


@masking_router.post("/segment")
async def segment_image(file: UploadFile = File(None),
    image_id: str = Form(None),                   # <- NEW (optional)
    db: AsyncSession = Depends(get_db),
    response_mode: str = Form("base64")  # NEW (optional)
):
    try:
        return await model_segment_image(file=file, image_id=image_id, db=db, response_mode=response_mode,)

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


@masking_router.post("/replace_material_advanced")
async def advanced_replace_material(
    original_image: str = Form(...),
    mask_image: str = Form(None),
    elements_json: str = Form(None),
    element_type: str = Form(None),
    element_id: str = Form(None),
    material_image: UploadFile = File(None),
    material_id: str = Form(None),
    method: str = Form("cv_poisson"),
    scale: float = Form(1.0),
    angle_bias_deg: float = Form(90.0),
    color_match: str = Form(None),
    preserve_shading: int = Form(1),
    # NEW: keeps current default behavior
    response_mode: str = Form("base64"),
):
    """
    Advanced material replacement with cv_poisson method.
    Supports both mask-based and element-based replacement.
    
    Parameters:
    - original_image: Base64 encoded original image (required)
    - mask_image: Base64 encoded mask image (optional, use with material_image)
    - elements_json: JSON string of house elements (optional, use with element_type)
    - element_type: Type of element to replace (optional, use with elements_json)
    - material_image: Uploaded material texture (optional)
    - material_id: Material ID from product catalog (optional, e.g., "Wall/categories/Brick/Red")
    - method: Replacement method (default: "cv_poisson")
    - scale: Scale factor for texture (default: 1.0)
    - angle_bias_deg: Angle bias for texture orientation (default: 90.0)
    - color_match: Color matching method ("reinhard" or None)
    - preserve_shading: Whether to preserve original shading (1=True, 0=False)
    
    Note: material_id will download the material image from the product catalog.
    Available material IDs include Wall, Accent, and Masonry categories with various materials.
    """
    try:
        # Validate that either material_image or material_id is provided, but not both
        if material_image is not None and material_id is not None:
            raise HTTPException(status_code=400, detail="Provide either material_image or material_id, not both")
        
        if material_image is None and material_id is None:
            raise HTTPException(status_code=400, detail="Provide either material_image or material_id")
        
        return model_advanced_replace_material(
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
        return HTTPException(status_code=500, detail=str(e))