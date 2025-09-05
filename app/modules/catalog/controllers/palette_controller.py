# app/modules/catalog/controllers/palette_controller.py

from fastapi import APIRouter, HTTPException
from app.modules.catalog.schemas.palattes_schema import (
    PaletteGroupSummary, PaletteGroup, PaletteItem, PaletteVariant
)
from app.modules.catalog.data.palattes_data import PALETTES

import re
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
    """Return all palette groups with their items (for the FE Palettes page)."""
    groups: list[PaletteGroup] = []

    for group_name, raw_items in PALETTES.items():
        items: list[PaletteItem] = []
        for it in raw_items:
            variants = [
                PaletteVariant(name=v["name"], slug=slugify(v["name"]))
                for v in it.get("variants", [])
            ]
            items.append(PaletteItem(
                name=it["name"],
                slug=slugify(it["name"]),
                image_url=it.get("image_url"),  # put thumbnails here later
                variants=variants               # stays empty for now
            ))

        groups.append(PaletteGroup(
            name=group_name,
            slug=slugify(group_name),
            items=items
        ))

    # sort groups by name to keep it stable (optional)
    groups.sort(key=lambda g: g.name.lower())
    return groups

@catalog_router.get("/palettes/{group_slug}", response_model=PaletteGroup)
async def get_palette_group(group_slug: str):
    # find matching group by slug
    match = None
    for group_name in PALETTES.keys():
        if slugify(group_name) == group_slug:
            match = group_name
            break
    if not match:
        raise HTTPException(status_code=404, detail="Palette group not found")

    items = []
    for item in PALETTES[match]:
        variants = [
            PaletteVariant(name=v["name"], slug=slugify(v["name"]))
            for v in item.get("variants", [])
        ]
        items.append(PaletteItem(
            name=item["name"],
            slug=slugify(item["name"]),
            image_url=item.get("image_url"),
            variants=variants
        ))

    return PaletteGroup(name=match, slug=group_slug, items=items)

@catalog_router.get("/palettes/{group_slug}/{item_slug}", response_model=PaletteItem)
async def get_palette_item(group_slug: str, item_slug: str):
    # Locate group
    group_name = None
    for g in PALETTES.keys():
        if slugify(g) == group_slug:
            group_name = g
            break
    if not group_name:
        raise HTTPException(status_code=404, detail="Palette group not found")

    # Locate item
    raw_item = None
    for it in PALETTES[group_name]:
        if slugify(it["name"]) == item_slug:
            raw_item = it
            break
    if not raw_item:
        raise HTTPException(status_code=404, detail="Palette item not found")

    variants = [
        PaletteVariant(name=v["name"], slug=slugify(v["name"]))
        for v in raw_item.get("variants", [])
    ]
    return PaletteItem(
        name=raw_item["name"],
        slug=item_slug,
        image_url=raw_item.get("image_url"),
        variants=variants
    )
