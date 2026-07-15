from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from sqlalchemy.orm import DeclarativeBase

from config import StorageConfig



# Ensure database folder exists
StorageConfig.DATABASE.parent.mkdir(
    parents=True,
    exist_ok=True
)



DATABASE_URL = (
    f"sqlite+aiosqlite:///{StorageConfig.DATABASE}"
)



engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)



AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)



class Base(DeclarativeBase):
    pass