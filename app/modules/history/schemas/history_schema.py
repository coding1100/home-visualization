# app/modules/history/schemas/history_schemas.py
import uuid
from datetime import datetime
from typing import Optional, Any, Dict, List

from pydantic import BaseModel, Field


class ImageEventOut(BaseModel):
    id: uuid.UUID
    session_id: Optional[str] = None
    user_id: Optional[uuid.UUID] = None

    base_image_id: Optional[uuid.UUID] = None
    base_image_url: str

    parent_event_id: Optional[uuid.UUID] = None

    tool: str

    element_type: Optional[str] = None
    material_slug: Optional[str] = None
    material_id: Optional[str] = None
    material_name: Optional[str] = None

    result_url: str
    annotated_url: Optional[str] = None

    params: Optional[Dict[str, Any]] = None
    created_at: datetime

    class Config:
        orm_mode = True


# class HistorySummaryOut(BaseModel):
#     original_image_url: Optional[str] = None
#     latest: Dict[str, Any] = Field(default_factory=dict)  # latest per element_type
#     timeline: List[ImageEventOut] = Field(default_factory=list)


class HistoryEventOut(BaseModel):
    id: str
    created_at: datetime
    session_id: Optional[str] = None
    user_id: Optional[str] = None
    base_image_id: Optional[str] = None
    base_image_url: Optional[str] = None
    tool: str
    element_type: Optional[str] = None
    material_slug: Optional[str] = None
    material_id: Optional[str] = None
    material_name: Optional[str] = None
    result_url: Optional[str] = None
    annotated_url: Optional[str] = None
    params: Optional[dict[str, Any]] = None

    class Config:
        orm_mode = True

class LatestPerCategoryItem(BaseModel):
    element_type: str
    result_url: Optional[str] = None
    annotated_url: Optional[str] = None
    material_slug: Optional[str] = None
    material_id: Optional[str] = None
    material_name: Optional[str] = None
    created_at: datetime

class HistorySummaryOut(BaseModel):
    latest_image_url: Optional[str] = None
    latest_by_category: Dict[str, LatestPerCategoryItem] = {}