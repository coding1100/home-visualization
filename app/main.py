# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.core.logging import setup_logging
from app.db.session import engine
from app.db.base import Base  # <-- add this import
from fastapi.middleware.cors import CORSMiddleware

from app.modules.signupflow.controllers.auth_controller import auth_router
from app.modules.billing.controllers.billing_controller import billing_router
from app.modules.contact.controllers.contact_controller import contact_router
from app.modules.files.controllers.file_controller import files_router
from app.modules.catalog.controllers.palette_controller import catalog_router
from app.modules.catalog.controllers.product_controller import products_simple_router
from app.modules.masking.controllers.masking_controller import masking_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    # Optional: prove DB connectivity on startup; harmless if DB isn't up yet
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
            # Detailed info (won't leak password)
            res = await conn.execute(text("""
                            select
                              inet_server_addr() as server_addr,
                              inet_server_port() as server_port,
                              inet_client_addr() as client_addr,
                              current_database() as db,
                              current_user as usr
                        """))
            print("DB CONNECTED TO:", res.mappings().first())
            # await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        # Don't crash the app if DB isn't reachable; log only.
        print("DB connectivity check failed:", repr(e))

        # pass
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # allow any origin
    allow_methods=["*"],     # allow any method (includes OPTIONS)
    allow_headers=["*"],     # allow any request headers
    allow_credentials=False, # must be False when allow_origins=["*"]
)

api_router = APIRouter(prefix=settings.API_PREFIX)   # -> /api/v1/*
api_router.include_router(auth_router)               # -> /api/v1/auth/*
api_router.include_router(billing_router)
api_router.include_router(contact_router)
api_router.include_router(files_router)
api_router.include_router(catalog_router)
api_router.include_router(products_simple_router)
api_router.include_router(masking_router)
app.include_router(api_router)