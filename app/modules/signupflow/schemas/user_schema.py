from pydantic import BaseModel, EmailStr, Field, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    confirm_password: str = Field(min_length=6)

    # FREE TEXT now
    role: str | None = Field(default=None, max_length=100)

    first_name: str
    last_name: str
    company_name: str | None = None
    contractor_builder_name: str | None = None
    phone: str | None = None
    address: str | None = None
    postal_code: str | None = None
    product_interest: str | None = None
    comments: str | None = None

    @field_validator("confirm_password")
    @classmethod
    def _passwords_match(cls, v, info):
        if info.data.get("password") != v:
            raise ValueError("Passwords do not match")
        return v

class UserOut(BaseModel):
    id: str
    email: EmailStr
    role: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    company_name: str | None = None
    contractor_builder_name: str | None = None
    phone: str | None = None
    address: str | None = None
    postal_code: str | None = None
    product_interest: str | None = None
    comments: str | None = None
    is_active: bool

    class Config:
        from_attributes = True
