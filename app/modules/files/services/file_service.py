import os
import uuid
import shutil
from pathlib import Path
from typing import Iterable

import cloudinary, cloudinary.uploader, cloudinary.utils
from fastapi import HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.modules.files.models.file_upload import FileUpload
from app.modules.files.s3utils.s3_utils import s3_upload_file
from app.modules.signupflow.models.user import User

# TMP_DIR = Path(settings.UPLOAD_TMP_DIR)
# TMP_DIR.mkdir(parents=True, exist_ok=True)

from pathlib import Path
from app.core.config import settings

# Normalize the path from .env
TMP_DIR = Path(settings.UPLOAD_TMP_DIR).expanduser()
if not TMP_DIR.is_absolute():
    # if someone sets a relative path, anchor it to the working dir
    TMP_DIR = (Path.cwd() / TMP_DIR).resolve()

# Create it (or fail with a clear message)
try:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
except PermissionError as e:
    raise RuntimeError(
        f"Cannot create temp dir {TMP_DIR}. "
        "Set UPLOAD_TMP_DIR to a writable absolute path and ensure the service user has permission."
    ) from e


MAX_BYTES = settings.UPLOAD_MAX_MB * 1024 * 1024

class FileService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _save_stream_to_disk(self, file: UploadFile, dst: Path) -> int:
        size = 0
        with dst.open("wb") as f:
            while True:
                chunk = await file.read(1024 * 1024)  # 1MB
                if not chunk:
                    break
                size += len(chunk)
                if size > MAX_BYTES:
                    try:
                        f.close()
                        dst.unlink(missing_ok=True)
                    except Exception:
                        pass
                    raise HTTPException(status_code=400, detail=f"File too large (>{settings.UPLOAD_MAX_MB}MB)")
                f.write(chunk)
        await file.seek(0)
        return size

    async def upload(self, *, file: UploadFile, session_id: str | None, user: User | None) -> FileUpload:
        # If user is logged in: upload to Cloudinary immediately (via temp file for size control)
        # Else: stage locally
        file_id = uuid.uuid4()
        temp_path = TMP_DIR / f"{file_id}_{file.filename}"

        # Save to temp (handles size enforcement)
        size = await self._save_stream_to_disk(file, temp_path)

        rec = FileUpload(
            id=file_id,
            session_id=session_id or "anonymous",
            user_id=user.id if user else None,
            filename=file.filename,
            content_type=file.content_type,
            size_bytes=size,
            temp_path=str(temp_path),
            status="staged" if user is None else "uploaded",
            storage="local" if user is None else "cloudinary",
        )
        self.db.add(rec)
        await self.db.flush()

        if user is None:
            # staged only
            await self.db.commit()
            return rec

        # authenticated: push to Cloudinary and finalize
        # try:
        #     res = cloudinary.uploader.upload(
        #         str(temp_path),
        #         folder=f"users/{user.id}",
        #         resource_type="auto",
        #         use_filename=True,
        #         unique_filename=True,
        #         overwrite=False,
        #     )
        # finally:
        #     try:
        #         temp_path.unlink(missing_ok=True)
        #     except Exception:
        #         pass

        # rec.public_id = res.get("public_id")
        # rec.secure_url = res.get("secure_url")
        # rec.storage = "cloudinary"
        # rec.status = "uploaded"
        # await self.db.commit()
        # await self.db.refresh(rec)
        # return rec

            # authenticated: push to S3 and finalize
        key = url = None
        try:
            key, url = s3_upload_file(str(temp_path), key_prefix=f"users/{user.id}")
        except Exception as e:
            # keep the same error surface as your cloudinary path used to
            raise HTTPException(status_code=502, detail=f"S3 upload failed: {e}")
        finally:
            try:
                temp_path.unlink(missing_ok=True)
            except Exception:
                pass

        if not key or not url:
            # extra guard to satisfy linters and avoid accidental None usage
            raise HTTPException(status_code=502, detail="S3 upload failed")

        rec.public_id = key          # S3 object key
        rec.secure_url = url         # public HTTPS url (or CloudFront)
        # keep the storage label unchanged for zero impact; switch to "s3" if desired
        rec.storage = "cloudinary"
        rec.status = "uploaded"
        await self.db.commit()
        await self.db.refresh(rec)
        return rec

    async def commit_one(self, *, upload_id: uuid.UUID, session_id: str, user: User) -> FileUpload:
        rec = await self.db.scalar(
            select(FileUpload).where(FileUpload.id == upload_id, FileUpload.session_id == session_id)
        )
        if not rec:
            raise HTTPException(status_code=404, detail="Upload not found for this session")
        if rec.status != "staged" or not rec.temp_path:
            # already uploaded or invalid state
            return rec

        # try:
        #     res = cloudinary.uploader.upload(
        #         rec.temp_path,
        #         folder=f"users/{user.id}",
        #         resource_type="auto",
        #         use_filename=True,
        #         unique_filename=True,
        #         overwrite=False,
        #     )
        #     # cleanup temp
        #     try:
        #         Path(rec.temp_path).unlink(missing_ok=True)
        #     except Exception:
        #         pass
        #
        #     rec.user_id = user.id
        #     rec.public_id = res.get("public_id")
        #     rec.secure_url = res.get("secure_url")
        #     rec.storage = "cloudinary"
        #     rec.status = "uploaded"
        #     rec.temp_path = None
        #     await self.db.commit()
        #     await self.db.refresh(rec)
        #     return rec
        # except cloudinary.exceptions.Error as e:
        #     raise HTTPException(status_code=502, detail=f"Cloudinary upload failed: {e}")

        try:
            key, url = s3_upload_file(rec.temp_path, key_prefix=f"users/{user.id}")
            # cleanup temp
            try:
                Path(rec.temp_path).unlink(missing_ok=True)
            except Exception:
                pass
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"S3 upload failed: {e}")

        if not key or not url:
            raise HTTPException(status_code=502, detail="S3 upload failed")

        rec.user_id = user.id
        rec.public_id = key
        rec.secure_url = url
        # keep the storage label unchanged for zero impact; switch to "s3" if desired
        rec.storage = "cloudinary"
        rec.status = "uploaded"
        rec.temp_path = None
        await self.db.commit()
        await self.db.refresh(rec)
        return rec


    async def commit_many(self, *, upload_ids: Iterable[uuid.UUID], session_id: str, user: User) -> list[FileUpload]:
        out: list[FileUpload] = []
        for uid in upload_ids:
            out.append(await self.commit_one(upload_id=uid, session_id=session_id, user=user))
        return out
