from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.modules.deps import get_db
from app.modules.signupflow.schemas.password_schema import ForgotPasswordRequest, ResetPasswordRequest
from app.modules.signupflow.schemas.user_schema import UserCreate, UserOut
from app.modules.signupflow.schemas.auth_schema import (
    LoginRequest, TokenPair, RefreshRequest, AccessTokenResponse
)
from app.modules.signupflow.services.service import UserService
from app.modules.signupflow.services.auth_services import AuthService
from app.security.tokens import create_access_token, create_refresh_token, decode_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await UserService(db).create_user(
        email=str(payload.email),
        password=payload.password,
        role=payload.role,
        first_name=payload.first_name,
        last_name=payload.last_name,
        company_name=payload.company_name,
        contractor_builder_name=payload.contractor_builder_name,
        phone=payload.phone,
        address=payload.address,
        postal_code=payload.postal_code,
        product_interest=payload.product_interest,
        comments=payload.comments,
    )
    return user

@auth_router.post("/login", response_model=TokenPair)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await AuthService(db).authenticate_user(str(payload.email), payload.password)
    return TokenPair(
        access_token=create_access_token(sub=str(user.id)),
        refresh_token=create_refresh_token(sub=str(user.id)),
    )

@auth_router.post("/refresh", response_model=AccessTokenResponse)
async def refresh(body: RefreshRequest):
    payload = decode_token(body.refresh_token, expected_type="refresh")
    return AccessTokenResponse(access_token=create_access_token(sub=payload["sub"]))


@auth_router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
async def forgot_password(payload: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    """
    Always returns 202 even if the email doesn't exist (no user enumeration).
    In ENV=dev we include the token in the response to help QA.
    """
    svc = AuthService(db)
    token = await svc.request_password_reset(str(payload.email))

    # TODO: send `token` by email. For now:
    if settings.ENV == "dev" and token:
        return {"message": "If the email exists, a reset link was sent.", "reset_token": token}

    return {"message": "If the email exists, a reset link was sent."}

@auth_router.post("/reset-password", status_code=status.HTTP_204_NO_CONTENT)
async def reset_password(payload: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    try:
        await AuthService(db).reset_password_with_token(payload.token, payload.new_password)
    except HTTPException:
        # pass through known errors
        raise
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")
    return  # 204