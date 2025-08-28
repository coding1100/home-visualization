from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.contact.models.contact_request import ContactRequest

class ContactService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, *, first_name: str, last_name: str, email: str, zip_code: str, role: str, details: str | None):
        rec = ContactRequest(
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            email=str(email).lower(),
            zip_code=zip_code.strip(),
            role=role.strip(),
            details=details,
        )
        self.db.add(rec)
        await self.db.commit()
        await self.db.refresh(rec)
        return rec
