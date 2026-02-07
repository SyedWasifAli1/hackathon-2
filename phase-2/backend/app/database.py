import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from contextlib import asynccontextmanager

# Import settings from config
from .config import settings

# Create async engine
def get_connect_args(database_url: str):
    """Get appropriate connection args based on database type"""
    if "sqlite" in database_url:
        return {"check_same_thread": False}
    elif "postgresql" in database_url:
        # For PostgreSQL/NeonDB, we may need specific connection args
        return {}
    else:
        return {}

engine: AsyncEngine = create_async_engine(
    settings.database_url,
    echo=True,  # Set to False in production
    # Disable pooling for SQLite
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    # Database-specific settings
    connect_args=get_connect_args(settings.database_url),
)


async def create_db_and_tables():
    """Create database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncSession:
    """Get async database session"""
    async with AsyncSession(engine) as session:
        yield session