import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Integer, DateTime, ForeignKey, func, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.modules.signupflow.models.user import User

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    user: Mapped[User | None] = relationship(lazy="joined")

    # Stripe references
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(String(255), index=True)
    stripe_payment_intent_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True, index=True)
    stripe_checkout_session_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True, index=True)
    stripe_charge_id: Mapped[Optional[str]] = mapped_column(String(255), index=True)

    # Business data
    amount: Mapped[Optional[int]] = mapped_column(Integer)  # minor units (cents)
    currency: Mapped[Optional[str]] = mapped_column(String(8))
    status: Mapped[str] = mapped_column(String(50), default="created")  # created|succeeded|processing|requires_payment_method|failed|refunded
    description: Mapped[Optional[str]] = mapped_column(String(500))

    raw: Mapped[Optional[dict]] = mapped_column(JSONB)  # full Stripe object snapshot

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    __table_args__ = (
        Index("ix_payments_user_status", "user_id", "status"),
    )