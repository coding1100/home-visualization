import uuid

from pydantic import BaseModel, EmailStr, Field

class ContactCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name:  str = Field(..., min_length=1, max_length=100)
    email:      EmailStr
    zip_code:   str = Field(..., min_length=2, max_length=20)
    role:       str = Field(..., min_length=2, max_length=50)  # e.g., Homeowner/Designer/etc.
    details:    str | None = Field(None, max_length=5000)

class ContactOut(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    zip_code: str
    role: str
    details: str | None = None

    model_config = {"from_attributes": True}
