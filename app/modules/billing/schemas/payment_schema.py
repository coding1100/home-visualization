import uuid
from datetime import datetime
from pydantic import BaseModel, Field

class PaymentOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID | None = None
    amount: int | None = None
    currency: str | None = None
    status: str
    stripe_customer_id: str | None = None
    stripe_payment_intent_id: str | None = None
    stripe_checkout_session_id: str | None = None
    stripe_charge_id: str | None = None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}

class LinkRequest(BaseModel):
    checkout_session_id: str | None = Field(default=None)
    payment_intent_id: str | None = Field(default=None)

    @property
    def has_any(self) -> bool:
        return bool(self.checkout_session_id or self.payment_intent_id)
