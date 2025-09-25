# app/core/config.py
import os
from urllib.parse import urlsplit

from dotenv import load_dotenv

load_dotenv(override=False)  # reads .env at project root
# load_dotenv()
def _mask_url(url: str) -> str:
    try:
        u = urlsplit(url)
        if "@" in u.netloc and ":" in u.netloc.split("@", 1)[0]:
            user = u.username or ""
            return url.replace(f"{user}:{u.password}", f"{user}:********")
    except Exception:
        pass
    return url

class Settings:
    # app
    ENV = os.getenv("ENV", "dev")
    API_PREFIX = os.getenv("API_PREFIX", "/api/v1")
    PROJECT_NAME = os.getenv("PROJECT_NAME", "Home Visualization API")

    # postgres pieces
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

    # full URLs (optional)
    # DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URI")
    DATABASE_URL = os.getenv("DATABASE_URL")

    # auth
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    # stripe
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")

    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    PASSWORD_RESET_TOKEN_MINUTES: int = 30

    UPLOAD_MAX_MB = int(os.getenv("UPLOAD_MAX_MB", "30"))
    UPLOAD_TMP_DIR = os.getenv("UPLOAD_TMP_DIR", "uploads/tmp")
    HF_TOKEN = os.getenv("HF_TOKEN")
    RF_API_KEY = os.getenv("RF_API_KEY")
    COMFYUI_SERVER = os.getenv("COMFYUI_SERVER")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    S3_BUCKET = os.getenv("S3_BUCKET")
    @property
    def db_url(self) -> str:
        """Async SQLAlchemy URL for our engine."""
        if self.DATABASE_URL:
            print(f"data base url in if condition: {self.DATABASE_URL}")
            return self.DATABASE_URL
        if all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_DB]):
            print(f"data base url in if all condition: {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )
        raise RuntimeError("Set DATABASE_URL or the POSTGRES_* pieces in .env")

    @property
    def masked_db_url(self) -> str:
        return _mask_url(self.db_url)

settings = Settings()


print(f"DATABASE_URL (masked): {settings.masked_db_url}")