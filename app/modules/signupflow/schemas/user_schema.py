import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)

class UserOut(UserBase):
    id: uuid.UUID
    is_active: bool
    stripe_customer_id: str | None = None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
