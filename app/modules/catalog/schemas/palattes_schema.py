# app/modules/catalog/schemas/palette_schema.py
from pydantic import BaseModel

class PaletteVariant(BaseModel):
    name: str
    slug: str

class PaletteItem(BaseModel):
    name: str
    slug: str
    image_url: str | None = None
    variants: list[PaletteVariant] = []

class PaletteGroupSummary(BaseModel):
    name: str
    slug: str
    count: int

class PaletteGroup(BaseModel):
    name: str
    slug: str
    items: list[PaletteItem]
