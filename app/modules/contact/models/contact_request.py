import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, func, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class ContactRequest(Base):
    __tablename__ = "contact_requests"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name:  Mapped[str] = mapped_column(String(100), nullable=False)
    email:      Mapped[str] = mapped_column(String(320), nullable=False, index=True)
    zip_code:   Mapped[str] = mapped_column(String(20), nullable=False)
    role:       Mapped[str] = mapped_column(String(50), nullable=False)   # “I am a”
    details:    Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    __table_args__ = (Index("ix_contact_email_created", "email", "created_at"),)
