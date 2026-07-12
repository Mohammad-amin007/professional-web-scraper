from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from storage.models import BookModel


class BookService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_books(self):
        result = await self.session.execute(
            select(BookModel)
        )

        return result.scalars().all()


    async def get_expensive_books(self, limit: int = 5):
        result = await self.session.execute(
            select(BookModel)
            .order_by(desc(BookModel.price))
            .limit(limit)
        )

        return result.scalars().all()


    async def search_books(self, keyword: str):
        result = await self.session.execute(
            select(BookModel)
            .where(
                BookModel.title.contains(keyword)
            )
        )

        return result.scalars().all()


    async def count_books(self):
        books = await self.get_all_books()

        return len(books)