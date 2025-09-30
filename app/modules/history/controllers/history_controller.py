# app/modules/history/controllers/history_controller.py
import uuid
from typing import Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, Header, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.deps import get_db, get_optional_user  # keep open; no auth dependency required
from app.modules.history.schemas.history_schema import HistorySummaryOut, ImageEventOut, LatestPerCategoryItem, \
    HistoryEventOut
from app.modules.history.services.history_service import HistoryService

history_router = APIRouter(prefix="/history", tags=["history"])

@history_router.get("/timeline", response_model=list[HistoryEventOut])
async def get_timeline(
    db: AsyncSession = Depends(get_db),
    session_id: Optional[str] = Header(default=None, alias="X-Session-Id"),
    current_user = Depends(get_optional_user),
):
    """
    Full, newest→oldest event list for this visitor.
    - Anonymous: pass X-Session-Id from FE.
    - Auth user: JWT will scope by user_id (preferred if both present).
    """
    svc = HistoryService(db)
    rows = await svc.timeline(
        session_id=session_id if not current_user else None,
        user_id=(current_user.id if current_user else None),
        limit=200,
    )
    return rows

@history_router.get("/summary", response_model=HistorySummaryOut)
async def get_summary(
    db: AsyncSession = Depends(get_db),
    session_id: Optional[str] = Header(default=None, alias="X-Session-Id"),
    current_user = Depends(get_optional_user),
):
    """
    Returns:
      - latest_image_url: the most recent produced image (segment/replace)
      - latest_by_category: dict {element_type -> most recent replacement event}
        so FE can render the latest 'Wall', 'Roof', etc., tiles like in your report screenshots.
    """
    svc = HistoryService(db)
    latest_url = await svc.latest_snapshot_url(
        session_id=session_id if not current_user else None,
        user_id=(current_user.id if current_user else None),
    )
    latest_map = await svc.latest_by_category(
        session_id=session_id if not current_user else None,
        user_id=(current_user.id if current_user else None),
    )

    out_map: Dict[str, LatestPerCategoryItem] = {}
    for k, ev in latest_map.items():
        out_map[k] = LatestPerCategoryItem(
            element_type=(ev.element_type or ""),
            result_url=ev.result_url,
            annotated_url=ev.annotated_url,
            material_slug=ev.material_slug,
            material_id=ev.material_id,
            material_name=ev.material_name,
            created_at=ev.created_at,
        )

    return HistorySummaryOut(latest_image_url=latest_url, latest_by_category=out_map)