from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.modules.signupflow.models.user import User
from app.security.passwords import hash_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(
        self,
        *,
        email: str,
        password: str,
        role: str | None,
        first_name: str,
        last_name: str,
        company_name: str | None = None,
        contractor_builder_name: str | None = None,
        phone: str | None = None,
        address: str | None = None,
        postal_code: str | None = None,
        product_interest: str | None = None,
        comments: str | None = None,
    ) -> User:
        existing = await self.db.scalar(select(User).where(User.email == email))
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

        full_name = f"{first_name} {last_name}".strip()

        user = User(
            email=email.lower().strip(),
            hashed_password=hash_password(password),

            role=role,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,

            company_name=company_name,
            contractor_builder_name=contractor_builder_name,
            phone=phone,
            address=address,
            postal_code=postal_code,
            product_interest=product_interest,
            comments=comments,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
