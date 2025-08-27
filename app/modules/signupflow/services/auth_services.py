from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.modules.signupflow.models.user import User
from app.security.passwords import verify_password, hash_password
from app.security.tokens import create_reset_token, decode_reset_token


class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def authenticate_user(self, email: str, password: str) -> User:
        # normalize email
        email = str(email).lower()

        user = await self.db.scalar(select(User).where(User.email == email))
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is inactive")

        return user

    async def request_password_reset(self, email: str) -> str | None:
        email = str(email).lower()
        user = await self.db.scalar(select(User).where(User.email == email))
        if not user:
            # Don't reveal whether email exists
            return None
        # Put user.id into the reset token
        return create_reset_token(sub=str(user.id))

    async def reset_password_with_token(self, token: str, new_password: str) -> None:
        payload = decode_reset_token(token)
        user_id = payload.get("sub")
        user = await self.db.scalar(select(User).where(User.id == user_id))
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
        user.hashed_password = hash_password(new_password)
        await self.db.commit()
