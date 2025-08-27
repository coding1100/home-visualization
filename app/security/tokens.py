from datetime import datetime, timedelta, timezone
from typing import Literal, Any, Dict

from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.core.config import settings

ALGORITHM = "HS256"

def _create_token(*, subject: str, minutes: int, ttype: Literal["access", "refresh"]) -> str:
    now = datetime.now(tz=timezone.utc)
    payload: Dict[str, Any] = {
        "sub": subject,
        "type": ttype,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=minutes)).timestamp()),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(sub: str) -> str:
    return _create_token(subject=sub, minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES, ttype="access")

# default refresh = 7 days if not set
REFRESH_MINUTES_DEFAULT = 60 * 24 * 7
def create_refresh_token(sub: str, minutes: int | None = None) -> str:
    minutes = minutes or REFRESH_MINUTES_DEFAULT
    return _create_token(subject=sub, minutes=minutes, ttype="refresh")

def decode_token(token: str, expected_type: Literal["access", "refresh"]) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != expected_type:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")


def create_reset_token(sub: str, minutes: int | None = None) -> str:
    minutes = minutes or settings.PASSWORD_RESET_TOKEN_MINUTES
    return _create_token(subject=sub, minutes=minutes, ttype="reset")

def decode_reset_token(token: str) -> dict:
    return decode_token(token, expected_type="reset")
