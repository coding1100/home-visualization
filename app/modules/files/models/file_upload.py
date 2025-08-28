import uuid
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import String, Integer, DateTime, ForeignKey, func, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.modules.signupflow.models.user import User

class FileUpload(Base):
    __tablename__ = "file_uploads"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    session_id: Mapped[str] = mapped_column(String(64), index=True)
    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    user: Mapped[User | None] = relationship(lazy="joined")

    status: Mapped[str] = mapped_column(String(20), default="staged")        # staged|uploaded|failed|deleted
    storage: Mapped[str] = mapped_column(String(20), default="local")         # local|cloudinary

    # local temp
    temp_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # cloudinary
    public_id: Mapped[Optional[str]] = mapped_column(String(255), index=True, unique=True)
    secure_url: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)

    # file meta
    filename: Mapped[Optional[str]] = mapped_column(String(255))
    content_type: Mapped[Optional[str]] = mapped_column(String(100))
    size_bytes: Mapped[Optional[int]] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.utcnow() + timedelta(hours=24))

    __table_args__ = (
        Index("ix_file_uploads_session_status", "session_id", "status"),
    )
