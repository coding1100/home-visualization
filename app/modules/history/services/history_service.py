# app/modules/history/services/history_service.py
import uuid
from typing import Optional, Any, Dict, List

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.history.models.image_event import ImageEvent


class HistoryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def record_event(
        self,
        *,
        session_id: Optional[str],
        user_id: Optional[uuid.UUID],
        base_image_id: Optional[uuid.UUID],
        base_image_url: str,
        tool: str,
        result_url: str,
        annotated_url: Optional[str] = None,
        element_type: Optional[str] = None,
        material_slug: Optional[str] = None,
        material_id: Optional[str] = None,
        material_name: Optional[str] = None,
        parent_event_id: Optional[uuid.UUID] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> ImageEvent:
        ev = ImageEvent(
            session_id=session_id,
            user_id=user_id,
            base_image_id=base_image_id,
            base_image_url=base_image_url,
            parent_event_id=parent_event_id,
            tool=tool,
            element_type=element_type,
            material_slug=material_slug,
            material_id=material_id,
            material_name=material_name,
            result_url=result_url,
            annotated_url=annotated_url,
            params=params or {},
        )
        self.db.add(ev)
        await self.db.commit()
        await self.db.refresh(ev)
        return ev

    async def get_summary(
        self,
        *,
        session_id: Optional[str] = None,
        user_id: Optional[uuid.UUID] = None,
        base_image_id: Optional[uuid.UUID] = None,
        base_image_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        if not session_id and not user_id:
            raise ValueError("Provide at least session_id or user_id")

        q = select(ImageEvent).order_by(desc(ImageEvent.created_at))
        if session_id:
            q = q.where(ImageEvent.session_id == session_id)
        if user_id:
            q = q.where(ImageEvent.user_id == user_id)
        if base_image_id:
            q = q.where(ImageEvent.base_image_id == base_image_id)
        if base_image_url:
            q = q.where(ImageEvent.base_image_url == base_image_url)

        rows = (await self.db.execute(q)).scalars().all()
        if not rows:
            return {"original_image_url": None, "latest": {}, "timeline": []}

        # timeline
        timeline: List[ImageEvent] = rows

        # original image = first event where tool == "upload" on this chain; fallback to most recent base_image_url
        original_url = None
        for ev in reversed(timeline):  # oldest -> newest
            if ev.tool == "upload":
                original_url = ev.result_url
                break
        if not original_url:
            original_url = timeline[-1].base_image_url  # oldest base url as fallback

        # latest per element_type
        latest: Dict[str, Any] = {}
        for ev in timeline:  # newest -> oldest
            if ev.element_type and ev.element_type not in latest:
                latest[ev.element_type] = {
                    "result_url": ev.result_url,
                    "material_slug": ev.material_slug,
                    "material_id": ev.material_id,
                    "material_name": ev.material_name,
                    "created_at": ev.created_at.isoformat(),
                }

        return {
            "original_image_url": original_url,
            "latest": latest,
            "timeline": rows,  # Pydantic will serialize via orm_mode
        }

    async def timeline(
            self,
            *,
            session_id: Optional[str] = None,
            user_id: Optional[uuid.UUID] = None,
            limit: int = 200
    ) -> List[ImageEvent]:
        """Return newest → oldest events for this visitor (anonymous via session or authed via user)."""
        stmt = select(ImageEvent).order_by(ImageEvent.created_at.desc())
        if user_id:
            stmt = stmt.where(ImageEvent.user_id == user_id)
        elif session_id:
            stmt = stmt.where(ImageEvent.session_id == session_id)
        rows = (await self.db.execute(stmt)).scalars().all()
        return rows[:limit]

    async def latest_by_category(
            self,
            *,
            session_id: Optional[str] = None,
            user_id: Optional[uuid.UUID] = None
    ) -> Dict[str, ImageEvent]:
        """
        Return a dict where the key is the element_type (e.g., 'wall', 'roof', 'masonry', etc.)
        and the value is the most recent replacement event for that category.
        """
        events = await self.timeline(session_id=session_id, user_id=user_id, limit=500)
        out: Dict[str, ImageEvent] = {}
        for ev in events:
            if ev.tool != "replace":
                continue
            et = (ev.element_type or "").strip().lower()
            if not et:
                continue
            # Pick the FIRST we see in newest→oldest ordering = most recent
            if et not in out:
                out[et] = ev
        return out

    async def latest_snapshot_url(
            self,
            *,
            session_id: Optional[str] = None,
            user_id: Optional[uuid.UUID] = None
    ) -> Optional[str]:
        """
        The most recent produced image (segment or replace). This is what the FE would
        consider the 'current' image.
        """
        events = await self.timeline(session_id=session_id, user_id=user_id, limit=1)
        if not events:
            return None
        # Prefer annotated_url when present; otherwise result_url.
        return events[0].annotated_url or events[0].result_url
