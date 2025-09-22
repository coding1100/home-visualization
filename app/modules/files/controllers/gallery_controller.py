# app/api/routes/gallery.py
import uuid
from uuid import UUID
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Header, status, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.modules.deps import get_db, get_current_user, get_optional_user
from app.modules.files.models.gallery_images import GalleryImage
from app.modules.signupflow.models.user import User
from app.modules.files.schemas.gallery_schemas import GalleryUploadOut, GalleryImageOut
from app.modules.files.services.file_service import FileService  # wherever your FileService lives
import cloudinary.uploader  # cloudinary is already configured in your app

gallery_router = APIRouter(prefix="/gallery", tags=["gallery"])

@gallery_router.post("/upload", response_model=GalleryUploadOut)
async def gallery_upload(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
        name: str | None = Form(None),
        session_id: str | None = Header(default=None, alias="X-Session-Id"),
):
    # 1) upload to Cloudinary (public)
    try:
        res = cloudinary.uploader.upload(
            file.file,                 # stream is fine here
            folder="gallery",          # public folder (no user context)
            resource_type="image",
            use_filename=True,
            unique_filename=True,
            overwrite=False,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")

    # 2) store in DB
    gi = GalleryImage(
        id=uuid.uuid4(),
        name=name or file.filename,
        url=res.get("secure_url"),
        public_id=res.get("public_id"),
        is_active=True,
    )
    db.add(gi)
    await db.commit()
    await db.refresh(gi)
    return gi


@gallery_router.get("", response_model=list[GalleryImageOut])
async def gallery_list(
    only_active: bool = True,
    db: AsyncSession = Depends(get_db),
):
    from sqlalchemy import select
    stmt = select(GalleryImage)
    if only_active:
        stmt = stmt.where(GalleryImage.is_active.is_(True))
    rows = (await db.execute(stmt)).scalars().all()
    return rows

@gallery_router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def gallery_delete(
    image_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    from sqlalchemy import select
    gi = (await db.execute(select(GalleryImage).where(GalleryImage.id == image_id))).scalar_one_or_none()
    if not gi:
        raise HTTPException(status_code=404, detail="Image not found")

    # Try to delete from Cloudinary if we have a public_id
    if gi.public_id:
        try:
            cloudinary.uploader.destroy(gi.public_id, invalidate=True)
        except Exception:
            # don't fail the API if Cloudinary destroy fails
            pass

    await db.delete(gi)
    await db.commit()
    return