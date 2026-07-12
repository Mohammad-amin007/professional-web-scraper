from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.book import Book
from storage.models import BookModel

from utils.logger import logger


class StorageService:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def save_or_update_book(
        self,
        book: Book
    ):

        try:

            result = await self.session.execute(
                select(BookModel).where(
                    BookModel.title == book.title
                )
            )

            existing_book = result.scalar_one_or_none()


            if existing_book:

                existing_book.price = book.price

                logger.info(
                    f"Updated book: {book.title}"
                )


            else:

                new_book = BookModel(
                    title=book.title,
                    price=book.price
                )

                self.session.add(new_book)

                logger.info(
                    f"Inserted book: {book.title}"
                )


        except Exception:

            logger.exception(
                f"Failed saving book: {book.title}"
            )

            raise



    async def save_books(
        self,
        books: list[Book]
    ):

        logger.info(
            f"Saving {len(books)} books to database."
        )


        try:

            for book in books:

                await self.save_or_update_book(
                    book
                )


            await self.session.commit()


            logger.info(
                "Database commit completed successfully."
            )


        except Exception:

            await self.session.rollback()

            logger.exception(
                "Database save failed."
            )

            raise