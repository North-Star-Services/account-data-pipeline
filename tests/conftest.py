import pytest_asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from revops import models  # noqa: F401
from revops.database import Base


async def make_session_factory():
    """Fresh in-memory database with all tables created."""
    engine = create_async_engine("sqlite+aiosqlite://", poolclass=StaticPool)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return engine, async_sessionmaker(engine, expire_on_commit=False)


@pytest_asyncio.fixture
async def session():
    engine, factory = await make_session_factory()
    async with factory() as s:
        yield s
    await engine.dispose()
