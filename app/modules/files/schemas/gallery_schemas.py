# app/schemas/gallery.py
from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel

class GalleryImageOut(BaseModel):
    id: UUID
    name: str
    url: str
    is_active: bool

class GalleryUploadOut(GalleryImageOut):
    pass
