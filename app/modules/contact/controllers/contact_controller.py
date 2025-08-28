from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.deps import get_db
from app.modules.contact.schemas.contact_schema import ContactCreate, ContactOut
from app.modules.contact.services.contact_service import ContactService

contact_router = APIRouter(prefix="/contact", tags=["contact"])

@contact_router.post("", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
async def create_contact(payload: ContactCreate, db: AsyncSession = Depends(get_db)):
    rec = await ContactService(db).create(
        first_name=payload.first_name,
        last_name=payload.last_name,
        email=str(payload.email),
        zip_code=payload.zip_code,
        role=payload.role,
        details=payload.details,
    )
    return rec
