# app/modules/catalog/controllers/products_controller.py
from __future__ import annotations
from typing import Any, Sequence, Union

from fastapi import APIRouter, HTTPException, Query

from app.modules.catalog.data.products_data import PRODUCTS_DATA
from app.modules.catalog.data.product_images import PRODUCT_IMAGE_MAP

products_simple_router = APIRouter(prefix="/catalog/products", tags=["catalog-products"])

@products_simple_router.get("/full")
async def products_full() -> dict:
    # keep the raw tree for power users/debug
    return PRODUCTS_DATA


def _img(path: str) -> Union[str, None]:
    return PRODUCT_IMAGE_MAP.get(path)


def _collapse_categories(node: Any, path: str) -> tuple[Any, str]:
    """
    If a dict has only {"categories": {...}}, auto-drill into it,
    but adjust the display path so children are under ".../categories".
    """
    if isinstance(node, dict) and set(node.keys()) == {"categories"}:
        return node["categories"], (path.rstrip("/") + "/categories") if path else "categories"
    return node, path


def _format_group(path: str, data: dict[str, Any]) -> dict:
    items = []
    for key, child in data.items():
        child_path = f"{path.rstrip('/')}/{key}" if path else key
        has_children = isinstance(child, dict)
        items.append({
            "name": key,
            "path": child_path,
            "has_children": has_children,
            "image_url": _img(child_path),
        })
    return {"path": path, "kind": "group", "items": items}


def _format_list(path: str, data: Sequence[str]) -> dict:
    items = []
    for name in data:
        child_path = f"{path.rstrip('/')}/{name}" if path else name
        items.append({
            "name": name,
            "path": child_path,
            "image_url": _img(child_path),
        })
    return {"path": path, "kind": "list", "items": items}


@products_simple_router.get("/node")
async def products_node(path: str = Query("")) -> Union[dict, Sequence, str]:
    """
    Browsing endpoint that always returns a list of displayable items:
      - GET /catalog/products/node?path=Wall
           -> { kind: "group", items: [ {name:"Brick", ...}, {name:"Siding", ...}, ...] }
      - GET /catalog/products/node?path=Wall/Siding
           -> group with Align/Aluminum/Steel/Vinyl/...
      - GET /catalog/products/node?path=Wall/Siding/Vinyl
           -> list of leaf options
    """
    # Walk the raw tree
    node: Any = PRODUCTS_DATA
    if path:
        for part in [p for p in path.split("/") if p]:
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                # Allow collapsing during traversal as well (e.g. "Wall" then "Brick")
                if isinstance(node, dict) and "categories" in node and part in node["categories"]:
                    node = node["categories"][part]
                else:
                    raise HTTPException(status_code=404, detail="Path not found")

    # Collapse {"categories": {...}} when present
    node, display_path = _collapse_categories(node, path)

    # Format
    if isinstance(node, dict):
        return _format_group(display_path, node)
    if isinstance(node, (list, tuple)):
        return _format_list(display_path, node)

    raise HTTPException(status_code=500, detail="Invalid node type")
