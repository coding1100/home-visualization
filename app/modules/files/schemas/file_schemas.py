import uuid
from pydantic import BaseModel, AnyUrl, Field
from typing import List

class UploadResponse(BaseModel):
    upload_id: uuid.UUID
    status: str
    secure_url: AnyUrl | None = None
    public_id: str | None = None
    filename: str | None = None
    size_bytes: int | None = None
    content_type: str | None = None

class CommitRequest(BaseModel):
    upload_ids: List[uuid.UUID] = Field(..., min_items=1)

class FileUploadOut(BaseModel):
    id: uuid.UUID
    status: str
    secure_url: AnyUrl | None = None
    public_id: str | None = None
    filename: str | None = None
    size_bytes: int | None = None
    content_type: str | None = None

    model_config = {"from_attributes": True}
