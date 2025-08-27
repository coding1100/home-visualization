from pydantic import BaseModel, EmailStr, Field

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str = Field(..., description="Password reset token from email")
    new_password: str = Field(..., min_length=8)
