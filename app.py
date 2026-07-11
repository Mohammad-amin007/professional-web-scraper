import asyncio

from database import AsyncSessionLocal, Base, engine

import storage.models

from scrapers.example_scraper import ExampleScraper
from services.storage_service import StorageService


async def main():

    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Run scraper
    scraper = ExampleScraper()

    books = scraper.run()

    print(f"Extracted books: {len(books)}")


    # Save data
    async with AsyncSessionLocal() as session:

        storage = StorageService(session)

        await storage.save_books(books)


    print("Books saved successfully")


if __name__ == "__main__":
    asyncio.run(main())