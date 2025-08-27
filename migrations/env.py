from __future__ import annotations
from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

# --- make 'app' importable when running alembic from project root ---
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # project root

from app.core.config import settings
from app.db.base import Base  # Base must import your models
from app.modules.signupflow.models.user import User
from app.modules.billing.models.payment import Payment


# Alembic Config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# inject our DB URL
config.set_main_option("sqlalchemy.url", settings.db_url)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=settings.db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    connectable: AsyncEngine = create_async_engine(settings.db_url, poolclass=pool.NullPool)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
