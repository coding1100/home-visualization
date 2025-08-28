import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.deps import get_db, get_current_user, get_optional_user
from app.modules.files.schemas.file_schemas import UploadResponse, CommitRequest, FileUploadOut
from app.modules.files.services.file_service import FileService
from app.modules.files.models.file_upload import FileUpload

files_router = APIRouter(prefix="/files", tags=["files"])

# ---- Unified upload: JWT -> immediate cloudinary; else requires X-Session-Id and stages locally
@files_router.post("/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(None),
    db: AsyncSession = Depends(get_db),
    opt_user = Depends(get_optional_user),
    session_id: str | None = Header(default=None, alias="X-Session-Id"),
):
    if not opt_user and not session_id:
        raise HTTPException(status_code=401, detail="Provide Authorization or X-Session-Id")

    if file is None:
        raise HTTPException(400, "Form-data part 'file' is required")

    rec = await FileService(db).upload(file=file, session_id=session_id, user=opt_user)
    return UploadResponse(
        upload_id=rec.id,
        status=rec.status,
        secure_url=rec.secure_url,
        public_id=rec.public_id,
        filename=rec.filename,
        size_bytes=rec.size_bytes,
        content_type=rec.content_type,
    )

# ---- Bulk commit staged uploads after login
@files_router.post("/commit", response_model=list[FileUploadOut])
async def commit_files(
    body: CommitRequest,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
    session_id: str | None = Header(default=None, alias="X-Session-Id"),
):
    if not session_id:
        raise HTTPException(status_code=400, detail="X-Session-Id header required")
    recs = await FileService(db).commit_many(upload_ids=body.upload_ids, session_id=session_id, user=current_user)
    return recs

# ---- Single commit (handy for FE)
@files_router.post("/{upload_id}/commit", response_model=FileUploadOut)
async def commit_one_file(
    upload_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
    session_id: str | None = Header(default=None, alias="X-Session-Id"),
):
    if not session_id:
        raise HTTPException(status_code=400, detail="X-Session-Id header required")
    rec = await FileService(db).commit_one(upload_id=upload_id, session_id=session_id, user=current_user)
    return rec

# ---- Download (redirect) by upload id
@files_router.get("/{upload_id}/download")
async def download_file(
    upload_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
):
    rec = await db.get(FileUpload, upload_id)
    if not rec:
        raise HTTPException(status_code=404, detail="File not found")
    if rec.status != "uploaded" or not rec.secure_url:
        raise HTTPException(status_code=409, detail="File not committed/uploaded yet")
    return RedirectResponse(rec.secure_url, status_code=307)
