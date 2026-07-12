from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from storage.models import BookModel

from utils.logger import logger


class BookService:

    def __init__(
        self,
        session: AsyncSession
    ):
        self.session = session


    async def get_all_books(self):

        logger.info(
            "Fetching all books from database."
        )

        try:

            result = await self.session.execute(
                select(BookModel)
            )

            books = result.scalars().all()

            logger.info(
                f"Retrieved {len(books)} books."
            )

            return books


        except Exception:

            logger.exception(
                "Failed fetching books."
            )

            raise



    async def get_expensive_books(
        self,
        limit: int = 5
    ):

        logger.info(
            f"Fetching top {limit} expensive books."
        )

        try:

            result = await self.session.execute(
                select(BookModel)
                .order_by(
                    desc(BookModel.price)
                )
                .limit(limit)
            )

            books = result.scalars().all()


            logger.info(
                f"Retrieved {len(books)} expensive books."
            )

            return books


        except Exception:

            logger.exception(
                "Failed fetching expensive books."
            )

            raise



    async def search_books(
        self,
        keyword: str
    ):

        logger.info(
            f"Searching books with keyword: {keyword}"
        )

        try:

            result = await self.session.execute(
                select(BookModel)
                .where(
                    BookModel.title.contains(keyword)
                )
            )

            books = result.scalars().all()


            logger.info(
                f"Search result count: {len(books)}"
            )

            return books


        except Exception:

            logger.exception(
                "Book search failed."
            )

            raise



    async def count_books(self):

        logger.info(
            "Counting books."
        )

        try:

            books = await self.get_all_books()

            count = len(books)

            logger.info(
                f"Total books count: {count}"
            )

            return count


        except Exception:

            logger.exception(
                "Counting books failed."
            )

            raise