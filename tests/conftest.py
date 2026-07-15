import pytest_asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from storage.models import BookModel



TEST_DATABASE_URL = (
    "sqlite+aiosqlite:///:memory:"
)



engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False
)


TestSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)



@pytest_asyncio.fixture
async def test_session():

    async with engine.begin() as conn:

        await conn.run_sync(
            BookModel.metadata.create_all
        )


    async with TestSessionLocal() as session:

        yield session


    async with engine.begin() as conn:

        await conn.run_sync(
            BookModel.metadata.drop_all
        )