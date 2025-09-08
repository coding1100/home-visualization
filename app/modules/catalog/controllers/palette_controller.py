# app/modules/catalog/controllers/palette_controller.py

from fastapi import APIRouter, HTTPException
from app.modules.catalog.schemas.palattes_schema import (
    PaletteGroupSummary, PaletteGroup, PaletteItem, PaletteVariant
)
from app.modules.catalog.data.palattes_data import PALETTES

import re
from app.modules.catalog.data.palettes_images import PALETTE_URLS


def _img_for(group_name: str, idx: int) -> str | None:
    urls = PALETTE_URLS.get(group_name, [])
    return urls[idx] if idx < len(urls) else None

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s

catalog_router = APIRouter(prefix="/catalog", tags=["catalog"])

@catalog_router.get("/palettes", response_model=list[PaletteGroupSummary])
async def list_palette_groups():
    out = []
    for group_name, items in PALETTES.items():
        out.append(PaletteGroupSummary(
            name=group_name,
            slug=slugify(group_name),
            count=len(items),
        ))
    return sorted(out, key=lambda x: x.name.lower())

@catalog_router.get("/palettes/full", response_model=list[PaletteGroup])
async def list_all_palette_groups_with_items():
    groups: list[PaletteGroup] = []
    for group_name, raw_items in PALETTES.items():
        items: list[PaletteItem] = []
        for i, it in enumerate(raw_items):
            variants = [
                PaletteVariant(name=v["name"], slug=slugify(v["name"]))
                for v in it.get("variants", [])
            ]
            items.append(PaletteItem(
                name=it["name"],
                slug=slugify(it["name"]),
                image_url=it.get("image_url") or _img_for(group_name, i),
                variants=variants
            ))
        groups.append(PaletteGroup(name=group_name, slug=slugify(group_name), items=items))
    groups.sort(key=lambda g: g.name.lower())
    return groups

@catalog_router.get("/palettes/{group_slug}", response_model=PaletteGroup)
async def get_palette_group(group_slug: str):
    match = next((g for g in PALETTES if slugify(g) == group_slug), None)
    if not match:
        raise HTTPException(status_code=404, detail="Palette group not found")

    items = []
    for i, it in enumerate(PALETTES[match]):
        variants = [
            PaletteVariant(name=v["name"], slug=slugify(v["name"]))
            for v in it.get("variants", [])
        ]
        items.append(PaletteItem(
            name=it["name"],
            slug=slugify(it["name"]),
            image_url=it.get("image_url") or _img_for(match, i),
            variants=variants
        ))
    return PaletteGroup(name=match, slug=group_slug, items=items)

@catalog_router.get("/palettes/{group_slug}/{item_slug}", response_model=PaletteItem)
async def get_palette_item(group_slug: str, item_slug: str):
    match = next((g for g in PALETTES if slugify(g) == group_slug), None)
    if not match:
        raise HTTPException(status_code=404, detail="Palette group not found")

    raw_items = PALETTES[match]
    idx = next((i for i, it in enumerate(raw_items) if slugify(it["name"]) == item_slug), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Palette item not found")

    raw_item = raw_items[idx]
    variants = [
        PaletteVariant(name=v["name"], slug=slugify(v["name"]))
        for v in raw_item.get("variants", [])
    ]
    return PaletteItem(
        name=raw_item["name"],
        slug=item_slug,
        image_url=raw_item.get("image_url") or _img_for(match, idx),
        variants=variants
    )
