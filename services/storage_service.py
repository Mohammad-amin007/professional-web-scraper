from sqlalchemy.ext.asyncio import AsyncSession

from models.book import Book
from storage.models import BookModel


class StorageService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_book(self, book: Book):
        db_book = BookModel(
            title=book.title,
            price=book.price,
        )

        self.session.add(db_book)

        await self.session.commit()

    async def save_books(self, books: list[Book]):
        for book in books:
            await self.save_book(book)