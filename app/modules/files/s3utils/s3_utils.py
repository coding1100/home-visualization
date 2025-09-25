# app/modules/files/services/s3_utils.py
import os, uuid, boto3
from datetime import datetime

from botocore.config import Config
from botocore.exceptions import ClientError
from app.core.config import settings

_session = None
_s3 = None

def get_s3():
    global _session, _s3
    if _s3 is None:
        _session = boto3.session.Session(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )
        _s3 = _session.client("s3", config=Config(signature_version="s3v4"))
    return _s3

def _public_base_url() -> str:
    bucket = settings.S3_BUCKET
    region = (settings.AWS_REGION or "us-east-1").strip()
    return f"https://{bucket}.s3.amazonaws.com" if region == "us-east-1" \
           else f"https://{bucket}.s3.{region}.amazonaws.com"

def s3_object_url(key: str) -> str:
    return f"{_public_base_url()}/{key.lstrip('/')}"

def s3_upload_file(path: str, key_prefix: str) -> tuple[str, str]:
    """Upload local file to S3; returns (key, url). No ACLs (bucket has ACLs disabled)."""
    s3 = get_s3()
    filename = os.path.basename(path)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    key = f"{key_prefix.rstrip('/')}/{ts}_{uuid.uuid4()}_{filename}"
    extra = {"ContentType": _guess_content_type(filename)}

    try:
        # IMPORTANT: no ACL here
        s3.upload_file(
            Filename=path,
            Bucket=settings.S3_BUCKET,
            Key=key,
            ExtraArgs=extra,
        )
    except ClientError as e:
        # If you ever reintroduce ACL by mistake, this makes the message clearer
        code = (e.response.get("Error") or {}).get("Code")
        if code in ("AccessControlListNotSupported", "InvalidRequest"):
            raise RuntimeError("Bucket has ACLs disabled. Remove any ACL usage from uploads.") from e
        raise

    return key, s3_object_url(key)

def s3_delete_object(key: str) -> None:
    get_s3().delete_object(Bucket=settings.S3_BUCKET, Key=key)

def _guess_content_type(name: str) -> str:
    ext = name.lower().rsplit(".", 1)[-1] if "." in name else ""
    return {
        "jpg": "image/jpeg", "jpeg": "image/jpeg",
        "png": "image/png",   "webp": "image/webp",
    }.get(ext, "application/octet-stream")
