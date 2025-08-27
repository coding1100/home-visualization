# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env at project root

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
    DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URI")

    # auth
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    # stripe
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
    PASSWORD_RESET_TOKEN_MINUTES: int = 30

    @property
    def db_url(self) -> str:
        """Async SQLAlchemy URL for our engine."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        if all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_DB]):
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )
        raise RuntimeError("Set DATABASE_URL or the POSTGRES_* pieces in .env")

settings = Settings()
