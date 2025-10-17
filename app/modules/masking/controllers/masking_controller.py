from typing import Optional

from app.modules.history.services.history_service import HistoryService
from src.model_functions import model_generate_mask, model_replace_material, model_segment_image, model_advanced_replace_material
from src.logger import logger
from fastapi import UploadFile, File, HTTPException, Form, APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.deps import get_db
masking_router = APIRouter(prefix="/masking", tags=["masking"])


@masking_router.post("/segment")
async def segment_image(file: UploadFile = File(None),
    image_id: str = Form(None),                   # <- NEW (optional)
    db: AsyncSession = Depends(get_db),
    session_id: Optional[str] = Header(default=None, alias="X-Session-Id"),
    response_mode: str = Form("base64")  # NEW (optional)
):
    try:
        return await model_segment_image(file=file, image_id=image_id, db=db, response_mode=response_mode,session_id=session_id, )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
        raise HTTPException(status_code=500, detail=str(e))


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
        raise HTTPException(status_code=500, detail=str(e))


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
    # NEW: orientation control parameters
    orientation_mode: str = Form("auto"),
    fixed_angle: float = Form(0.0),
    # NEW: keeps current default behavior
    response_mode: str = Form("base64"),
    db: AsyncSession =Depends(get_db),
    session_id: Optional[str] = Header(default=None, alias="X-Session-Id"),
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
    - orientation_mode: Texture orientation mode ("auto" or "fixed", default: "auto")
    - fixed_angle: Fixed angle for texture when orientation_mode="fixed" (default: 0.0)
    
    Note: material_id will download the material image from the product catalog.
    Available material IDs include Wall, Accent, and Masonry categories with various materials.
    """
    try:
        # Validate that either material_image or material_id is provided, but not both
        if material_image is None and material_id is None:
            raise HTTPException(status_code=400, detail="Provide either material_image or material_id")
        
        res = model_advanced_replace_material(
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
            orientation_mode=orientation_mode,
            fixed_angle=fixed_angle,
            response_mode=response_mode,

        )
        if (
                isinstance(res, dict)
                and res.get("success") is True
                and str(response_mode).lower() == "url"
                and method == "cv_poisson"
        ):
            replaced_image_url = res.get("replaced_image_url") or res.get("result_url")
            if replaced_image_url:
                try:
                    await HistoryService(db).record_event(
                        session_id=session_id,  # pass session id if you have it
                        user_id=None,  # pass user id if you have it
                        base_image_id=None,  # if you know the gallery image id, set it; else None
                        base_image_url=original_image,  # controller receives the original image URL
                        tool="replace",
                        element_type=(element_type or None),
                        material_slug=None,  # set if you can build e.g. "Wall/categories/Brick/Red"
                        material_id=material_id,
                        material_name=None,
                        result_url=replaced_image_url,
                        params={
                            "scale": scale,
                            "angle_bias_deg": angle_bias_deg,
                            "color_match": color_match,
                            "preserve_shading": bool(int(preserve_shading)),
                            "method": method,
                        },
                    )
                except Exception:
                    # do not break the API if history write fails
                    pass

        return res
    except Exception as e:
        logger.error(f"ControllerError in advanced material replacement: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))