# app/modules/history/controllers/history_controller.py
import io
from typing import Optional, Dict, Tuple

import requests
from fastapi import APIRouter, Depends, Header
from fastapi.responses import Response
from reportlab.lib.colors import black, HexColor
from sqlalchemy.ext.asyncio import AsyncSession
from reportlab.pdfgen import canvas
from PIL import Image
from datetime import datetime

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader


from app.modules.deps import get_db, get_optional_user  # keep open; no auth dependency required
from app.modules.history.schemas.history_schema import HistorySummaryOut, LatestPerCategoryItem, \
    HistoryEventOut
from app.modules.history.services.history_service import HistoryService
from src.material_service import download_material_image_binary

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

BRAND_IMAGE_URL = "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-075648_22ce3b2c-7766-4a27-b56f-42103399498d_85b78257-d023-4a4b-85b4-6522d6b44a0e_landingPageImg.jpg"
COMPANY_LOGO_URL = "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png"

DISCLAIMER_TEXT = (
    "Products and colors may not be exactly as shown. This is due to a variance in monitor calibrations. "
    "Please base your color selection on actual samples before making your final decision."
)

# ---------- helpers ----------

def _fetch_image_bytes(url: str) -> Optional[bytes]:
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        return r.content
    except Exception:
        return None

def _to_reader_rgb(img_bytes: bytes) -> ImageReader:
    img = Image.open(io.BytesIO(img_bytes))
    if img.mode in ("RGBA", "LA"):
        # flatten transparency onto white
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    else:
        img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return ImageReader(buf)

def _fit(w: float, h: float, max_w: float, max_h: float) -> Tuple[float, float]:
    if w <= 0 or h <= 0:
        return max_w, max_h
    s = min(max_w / w, max_h / h)
    return w * s, h * s

def _draw_centered_reader(c: canvas.Canvas, reader: ImageReader, x: float, y: float, box_w: float, box_h: float):
    iw, ih = reader.getSize()
    tw, th = _fit(iw, ih, box_w, box_h)
    c.drawImage(reader, x + (box_w - tw) / 2.0, y + (box_h - th) / 2.0, width=tw, height=th, preserveAspectRatio=True, mask='auto')

def _draw_text(c: canvas.Canvas, text: str, x_center: float, y: float, size: int = 12, bold: bool = False):
    c.setFillColor(black)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    c.drawCentredString(x_center, y, text)

def _material_card(c: canvas.Canvas, x: float, y: float, w: float, h: float,
                   name_lines: list[str], swatch_bytes: Optional[bytes]):
    """
    Draw a material card with an image on the left and text lines on the right.
    (x,y) = bottom-left. w,h in points.
    """
    padding = 8
    img_box_w = 80
    img_box_h = h - 2 * padding
    text_x = x + padding + img_box_w + 10
    text_y = y + h - padding - 12
    # frame (optional)
    c.setStrokeColor(HexColor("#DDDDDD"))
    c.rect(x, y, w, h, stroke=1, fill=0)

    # swatch
    if swatch_bytes:
        try:
            reader = _to_reader_rgb(swatch_bytes)
            _draw_centered_reader(c, reader, x + padding, y + padding, img_box_w, img_box_h)
        except Exception:
            # gray placeholder
            c.setFillColor(HexColor("#F0F0F0"))
            c.rect(x + padding, y + padding, img_box_w, img_box_h, stroke=0, fill=1)
            c.setFillColor(black)
    else:
        c.setFillColor(HexColor("#F0F0F0"))
        c.rect(x + padding, y + padding, img_box_w, img_box_h, stroke=0, fill=1)
        c.setFillColor(black)

    # text
    c.setFont("Helvetica", 10)
    for line in name_lines:
        c.drawString(text_x, text_y, line)
        text_y -= 13

@history_router.get("/report.pdf")
async def report_pdf(
    db: AsyncSession = Depends(get_db),
    session_id: Optional[str] = Header(default=None, alias="X-Session-Id"),
    current_user = Depends(get_optional_user),
) -> Response:
    """
    Multi-page PDF:
      1) Cover: title, date, brand image, logo
      2) Latest rendered image + latest-by-category materials (grid)
      3..N) Remaining materials (grid only) if they don't fit on page 2
      Last) Logo + disclaimer
    """
    PAGE_W, PAGE_H = LETTER  # 612 x 792
    MARGIN = 32
    HEADER_GAP = 48
    FOOTER_GAP = 48

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=LETTER)

    # ------------------------------------------------------------------------------------
    # COVER
    # ------------------------------------------------------------------------------------
    _draw_text(c, "Design Report", PAGE_W / 2, PAGE_H - MARGIN - 20, size=22, bold=True)
    _draw_text(c, datetime.now().strftime("%d %b %Y"), PAGE_W / 2, PAGE_H - MARGIN - 40, size=10, bold=False)

    brand_bytes = _fetch_image_bytes(BRAND_IMAGE_URL)
    logo_bytes = _fetch_image_bytes(COMPANY_LOGO_URL)

    if brand_bytes:
        brand_reader = _to_reader_rgb(brand_bytes)
        # area between header and footer (reserve space for logo)
        logo_h_target = 160.0
        brand_top = PAGE_H - MARGIN - 60
        brand_bottom = MARGIN + logo_h_target + 16
        brand_avail_h = max(80.0, brand_top - brand_bottom)
        _draw_centered_reader(c, brand_reader, MARGIN, brand_bottom, PAGE_W - 2 * MARGIN, brand_avail_h)

    if logo_bytes:
        logo_reader = _to_reader_rgb(logo_bytes)
        lw, lh = logo_reader.getSize()
        tw, th = _fit(lw, lh, 240, 120)
        _draw_centered_reader(c, logo_reader, (PAGE_W - tw) / 2, MARGIN, tw, th)

    c.showPage()

    # ------------------------------------------------------------------------------------
    # DATA FROM HISTORY
    # ------------------------------------------------------------------------------------
    svc = HistoryService(db)
    viewer_session = None if current_user else session_id
    viewer_user_id = current_user.id if current_user else None

    latest_url = await svc.latest_snapshot_url(session_id=viewer_session, user_id=viewer_user_id)
    latest_map = await svc.latest_by_category(session_id=viewer_session, user_id=viewer_user_id)
    # latest_map: Dict[str, HistoryEvent]

    # ------------------------------------------------------------------------------------
    # PAGE 2: Latest image + first chunk of materials
    # ------------------------------------------------------------------------------------
    # TITLE
    _draw_text(c, "Latest Design", PAGE_W / 2, PAGE_H - MARGIN - 16, size=16, bold=True)

    # latest image area
    image_top_y = PAGE_H - MARGIN - 40
    image_box_h = 360
    image_box_w = PAGE_W - 2 * MARGIN
    image_y = image_top_y - image_box_h

    if latest_url:
        img_bytes = _fetch_image_bytes(latest_url)
        if img_bytes:
            reader = _to_reader_rgb(img_bytes)
            _draw_centered_reader(c, reader, MARGIN, image_y, image_box_w, image_box_h)
    # materials heading
    _draw_text(c, "Latest Applied Materials", PAGE_W / 2, image_y - 16, size=12, bold=True)

    # grid params
    grid_top = image_y - 36
    row_h = 90
    col_w = (PAGE_W - 2 * MARGIN - 16) / 2  # 2 columns, 16pts gutter
    x_cols = [MARGIN, MARGIN + col_w + 16]

    # paginate materials
    materials = []
    for k, ev in latest_map.items():
        # Build label lines
        lines = []
        # Try to keep four lines like your screenshots: Category / Subcat / Brand / Name
        if ev.material_slug:
            parts = [p for p in ev.material_slug.split("/") if p]
            # Show up to 4 lines from slug parts
            for p in parts[:4]:
                lines.append(p)
        elif ev.material_name:
            lines.append(ev.material_name)
        else:
            # fallback to element type
            lines.append(ev.element_type or "Material")

        # fetch swatch bytes if possible
        swatch = None
        if download_material_image_binary and ev.material_id:
            try:
                swatch = download_material_image_binary(ev.material_id)
            except Exception:
                swatch = None

        materials.append((lines, swatch))

    # draw as many as fit on this page
    y = grid_top
    col = 0
    idx = 0
    per_page_first = int((grid_top - MARGIN - FOOTER_GAP) // row_h) * 2  # rough calc, two columns

    while idx < len(materials):
        # choose how many fit on page
        max_rows = int((y - (MARGIN + FOOTER_GAP)) // row_h)
        slots = max_rows * 2  # two columns
        if slots <= 0:
            c.showPage()
            y = PAGE_H - MARGIN
            _draw_text(c, "Materials", PAGE_W / 2, PAGE_H - MARGIN - 16, size=16, bold=True)
            continue

        # draw this page chunk
        for _ in range(slots):
            if idx >= len(materials):
                break
            lines, swatch = materials[idx]
            _material_card(c, x_cols[col], y - row_h, col_w, row_h, lines, swatch)
            col = 1 - col
            if col == 0:
                y -= row_h
            idx += 1

        if idx < len(materials):
            c.showPage()
            y = PAGE_H - MARGIN
            _draw_text(c, "Materials", PAGE_W / 2, PAGE_H - MARGIN - 16, size=16, bold=True)

    # ------------------------------------------------------------------------------------
    # LAST PAGE: logo + disclaimer
    # ------------------------------------------------------------------------------------
    c.showPage()
    if logo_bytes:
        logo_reader = _to_reader_rgb(logo_bytes)
        lw, lh = logo_reader.getSize()
        tw, th = _fit(lw, lh, 240, 120)
        _draw_centered_reader(c, logo_reader, (PAGE_W - tw) / 2, (PAGE_H / 2) - (th / 2) + 40, tw, th)

    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    text_wrap = 70  # characters per line approximate
    # simple wrap
    import textwrap
    lines = textwrap.wrap(DISCLAIMER_TEXT, width=90)
    y_text = 120
    for line in lines:
        _draw_text(c, line, PAGE_W / 2, y_text, size=10, bold=False)
        y_text -= 14

    # finalize
    c.save()
    pdf_bytes = buf.getvalue()
    buf.close()

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=design-report.pdf"},
    )

