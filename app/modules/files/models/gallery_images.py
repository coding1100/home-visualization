# app/models/gallery_image.py
import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base  # same Base you use for FileUpload

class GalleryImage(Base):
    __tablename__ = "gallery_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    url = Column(String, nullable=False)          # Cloudinary secure URL
    is_active = Column(Boolean, nullable=False, default=True)

    # keep Cloudinary public_id internally so hard delete is possible if you ever want it
    public_id = Column(String(255), nullable=True)
