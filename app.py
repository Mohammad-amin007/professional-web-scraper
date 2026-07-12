import asyncio

from database import AsyncSessionLocal, Base, engine

import storage.models

from scrapers.example_scraper import ExampleScraper
from services.storage_service import StorageService
from services.book_service import BookService


async def main():

    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Run scraper
    scraper = ExampleScraper()

    books = scraper.run()

    print(f"Extracted books: {len(books)}")


    # Database session
    async with AsyncSessionLocal() as session:

        storage = StorageService(session)

        await storage.save_books(books)

        print("Books saved successfully")


        book_service = BookService(session)

        all_books = await book_service.get_all_books()

        print(
            f"Database books: {len(all_books)}"
        )

        for book in all_books[:5]:
            print(
                book.title,
                book.price
            )


    # Close database connections
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())