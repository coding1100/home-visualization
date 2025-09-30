# app/modules/history/models/image_event.py
import uuid
from datetime import datetime

from sqlalchemy import Column, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.db.base import Base  # <- same base your other models use


class ImageEvent(Base):
    __tablename__ = "image_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # link to anonymous session / user (both optional; at least one usually present)
    session_id = Column(Text, nullable=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True, index=True)

    # base image (what we started from)
    base_image_id = Column(UUID(as_uuid=True), ForeignKey("gallery_images.id"), nullable=True, index=True)
    base_image_url = Column(Text, nullable=False, index=True)

    # parent event (optional, for chaining if you want)
    parent_event_id = Column(UUID(as_uuid=True), ForeignKey("image_events.id"), nullable=True, index=True)

    # what happened
    tool = Column(Text, nullable=False)  # "upload" | "segment" | "replace"

    # material application details (for replace)
    element_type = Column(Text, nullable=True)      # e.g. "wall", "roof"
    material_slug = Column(Text, nullable=True)     # e.g. "Wall/categories/Brick/Red"
    material_id = Column(Text, nullable=True)
    material_name = Column(Text, nullable=True)

    # results
    result_url = Column(Text, nullable=False)       # resulting image for this event
    annotated_url = Column(Text, nullable=True)     # segmentation overlay if applicable

    # optional bag for params (scale, color_match, etc.)
    params = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, index=True)

    # optional relationships (not required to function)
    # user = relationship("User")
    # base_image = relationship("GalleryImage", foreign_keys=[base_image_id])
