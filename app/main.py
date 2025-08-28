# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.core.logging import setup_logging
from app.db.session import engine
from app.modules.signupflow.controllers.auth_controller import auth_router
from app.modules.billing.controllers.billing_controller import billing_router
from app.modules.contact.controllers.contact_controller import contact_router
from app.modules.files.controllers.file_controller import files_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    # Optional: prove DB connectivity on startup; harmless if DB isn't up yet
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception:
        # Don't crash the app if DB isn't reachable; log only.
        pass
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.1",
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=None,
    lifespan=lifespan,
)

# (Optional) Debug: log the routes on startup so you can see what's registered
from fastapi.routing import APIRoute
for r in app.routes:
    if isinstance(r, APIRoute):
        methods = ",".join(sorted(r.methods))
        print(f"[ROUTE] {methods:10s} {r.path}")

api_router = APIRouter(prefix=settings.API_PREFIX)   # -> /api/v1/*
api_router.include_router(auth_router)               # -> /api/v1/auth/*
api_router.include_router(billing_router)
api_router.include_router(contact_router)
api_router.include_router(files_router)
app.include_router(api_router)