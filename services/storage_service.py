from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.book import Book
from storage.models import BookModel


class StorageService:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def save_or_update_book(self, book: Book):

        result = await self.session.execute(
            select(BookModel).where(
                BookModel.title == book.title
            )
        )

        existing_book = result.scalar_one_or_none()


        if existing_book:
            # Update existing record
            existing_book.price = book.price

        else:
            # Insert new record
            new_book = BookModel(
                title=book.title,
                price=book.price
            )

            self.session.add(new_book)


    async def save_books(self, books: list[Book]):

        for book in books:
            await self.save_or_update_book(book)

        await self.session.commit()