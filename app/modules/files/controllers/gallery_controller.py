# # app/api/routes/gallery.py
# import uuid
# from uuid import UUID
# from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Header, status, Form
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select, update
#
# from app.modules.deps import get_db, get_current_user, get_optional_user
# from app.modules.files.models.gallery_images import GalleryImage
# from app.modules.signupflow.models.user import User
# from app.modules.files.schemas.gallery_schemas import GalleryUploadOut, GalleryImageOut
# from app.modules.files.services.file_service import FileService  # wherever your FileService lives
# import cloudinary.uploader  # cloudinary is already configured in your app
#
# gallery_router = APIRouter(prefix="/gallery", tags=["gallery"])
#
# @gallery_router.post("/upload", response_model=GalleryUploadOut)
# async def gallery_upload(
#     file: UploadFile = File(...),
#     db: AsyncSession = Depends(get_db),
#         name: str | None = Form(None),
#         session_id: str | None = Header(default=None, alias="X-Session-Id"),
# ):
#     # 1) upload to Cloudinary (public)
#     try:
#         res = cloudinary.uploader.upload(
#             file.file,                 # stream is fine here
#             folder="gallery",          # public folder (no user context)
#             resource_type="image",
#             use_filename=True,
#             unique_filename=True,
#             overwrite=False,
#         )
#     except Exception as e:
#         raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")
#
#     # 2) store in DB
#     gi = GalleryImage(
#         id=uuid.uuid4(),
#         name=name or file.filename,
#         url=res.get("secure_url"),
#         public_id=res.get("public_id"),
#         is_active=True,
#     )
#     db.add(gi)
#     await db.commit()
#     await db.refresh(gi)
#     return gi
#
#
# @gallery_router.get("", response_model=list[GalleryImageOut])
# async def gallery_list(
#     only_active: bool = True,
#     db: AsyncSession = Depends(get_db),
# ):
#     from sqlalchemy import select
#     stmt = select(GalleryImage)
#     if only_active:
#         stmt = stmt.where(GalleryImage.is_active.is_(True))
#     rows = (await db.execute(stmt)).scalars().all()
#     return rows
#
# @gallery_router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def gallery_delete(
#     image_id: uuid.UUID,
#     db: AsyncSession = Depends(get_db),
# ):
#     from sqlalchemy import select
#     gi = (await db.execute(select(GalleryImage).where(GalleryImage.id == image_id))).scalar_one_or_none()
#     if not gi:
#         raise HTTPException(status_code=404, detail="Image not found")
#
#     # Try to delete from Cloudinary if we have a public_id
#     if gi.public_id:
#         try:
#             cloudinary.uploader.destroy(gi.public_id, invalidate=True)
#         except Exception:
#             # don't fail the API if Cloudinary destroy fails
#             pass
#
#     await db.delete(gi)
#     await db.commit()
#     return







import uuid
import shutil
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.deps import get_db
from app.core.config import settings
from app.modules.files.models.gallery_images import GalleryImage
from app.modules.files.schemas.gallery_schemas import GalleryImageOut
from app.modules.files.s3utils.s3_utils import s3_upload_file, get_s3

gallery_router = APIRouter(prefix="/gallery", tags=["gallery"])

# ---- temp dir + size limit (same policy as file_service) ----
TMP_DIR = Path(settings.UPLOAD_TMP_DIR).expanduser()
if not TMP_DIR.is_absolute():
    TMP_DIR = (Path.cwd() / TMP_DIR).resolve()
TMP_DIR.mkdir(parents=True, exist_ok=True)

MAX_BYTES = settings.UPLOAD_MAX_MB * 1024 * 1024  # e.g. 30 MB

async def _save_stream_to_disk(file: UploadFile, dst: Path) -> int:
    """Save UploadFile to disk enforcing MAX_BYTES; returns size."""
    size = 0
    with dst.open("wb") as f:
        while True:
            chunk = await file.read(1024 * 1024)  # 1 MB chunks
            if not chunk:
                break
            size += len(chunk)
            if size > MAX_BYTES:
                try:
                    f.close()
                    dst.unlink(missing_ok=True)
                except Exception:
                    pass
                raise HTTPException(status_code=400, detail=f"File too large (>{settings.UPLOAD_MAX_MB}MB)")
            f.write(chunk)
    await file.seek(0)
    return size


# ------------------------ POST /gallery/upload ------------------------
@gallery_router.post("/upload", response_model=GalleryImageOut, status_code=status.HTTP_201_CREATED)
async def gallery_upload(
    file: UploadFile = File(...),
    name: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Open endpoint: upload a public gallery image to S3 and record it in DB.
    """
    # 1) save to temp (size enforced)
    image_id = uuid.uuid4()
    temp_path = TMP_DIR / f"{image_id}_{file.filename}"
    await _save_stream_to_disk(file, temp_path)

    # 2) push to S3
    key = url = None
    try:
        # store under 'gallery/' prefix
        key, url = s3_upload_file(str(temp_path), key_prefix="gallery")
    except Exception as e:
        # make sure temp file is cleaned even on failure
        try:
            temp_path.unlink(missing_ok=True)
        except Exception:
            pass
        raise HTTPException(status_code=502, detail=f"S3 upload failed: {e}")
    finally:
        try:
            temp_path.unlink(missing_ok=True)
        except Exception:
            pass

    if not key or not url:
        raise HTTPException(status_code=502, detail="S3 upload failed")

    # 3) store in DB
    gi = GalleryImage(
        id=image_id,
        name=name or file.filename,
        public_id=key,      # S3 object key
        url=url,     # public https url (or CloudFront)
        is_active=True,
    )
    db.add(gi)
    await db.commit()
    await db.refresh(gi)
    return gi


# -------------------------- GET /gallery --------------------------
@gallery_router.get("", response_model=list[GalleryImageOut])
async def list_gallery(
    db: AsyncSession = Depends(get_db),
    include_inactive: bool = Query(False, description="Include inactive rows when true"),
):
    """
    Open endpoint: list gallery images (active by default).
    """
    stmt = select(GalleryImage)
    if not include_inactive:
        stmt = stmt.where(GalleryImage.is_active.is_(True))
    rows = (await db.execute(stmt)).scalars().all()
    return rows


# --------------------- DELETE /gallery/{image_id} --------------------
@gallery_router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def gallery_delete(image_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    gi = (await db.execute(select(GalleryImage).where(GalleryImage.id == image_id))).scalar_one_or_none()
    if not gi:
        raise HTTPException(status_code=404, detail="Image not found")

    # Try to delete from S3 if we have a key (public_id)
    if gi.public_id:
        try:
            s3 = get_s3()
            s3.delete_object(Bucket=settings.S3_BUCKET, Key=gi.public_id)
        except Exception:
            # don’t fail API if S3 delete fails (same leniency as before)
            pass

    await db.delete(gi)
    await db.commit()
    return
