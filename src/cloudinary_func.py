import cloudinary
from app.core.config import settings


def ensure_cloudinary_config():
    cfg = cloudinary.config()
    if not cfg.api_key or not cfg.api_secret or not cfg.cloud_name:
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True,
        )
        
def upload_image_to_cloudinary(output_binary, element_type = None):
    folder_parts = ["renders"]
    if element_type:
        folder_parts.append(str(element_type).lower())
    upload_folder = "/".join(folder_parts)

    res = cloudinary.uploader.upload(
        output_binary,
        folder=upload_folder,
        resource_type="auto",
        use_filename=True,
        unique_filename=True,
        overwrite=False,
    )
    return res