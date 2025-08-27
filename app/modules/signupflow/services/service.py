from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.modules.signupflow.models.user import User
from app.security.passwords import hash_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, *, email: str, password: str, full_name: str | None) -> User:
        # uniqueness check
        existing = await self.db.scalar(select(User).where(User.email == email))
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

        user = User(
            email=email,
            hashed_password=hash_password(password),
            full_name=full_name,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
