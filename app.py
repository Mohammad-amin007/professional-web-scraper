import asyncio

from database import AsyncSessionLocal, Base, engine

import storage.models

from scrapers.example_scraper import ExampleScraper

from services.storage_service import StorageService
from services.book_service import BookService
from services.export_service import ExportService


async def main():

    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

    print("Database ready.")


    # Run scraper
    scraper = ExampleScraper()

    books = scraper.run()

    print(
        f"Extracted books: {len(books)}"
    )


    async with AsyncSessionLocal() as session:

        # Save or update books
        storage_service = StorageService(
            session
        )

        await storage_service.save_books(
            books
        )

        print(
            "Books saved successfully"
        )


        # Read books from database
        book_service = BookService(
            session
        )

        all_books = await book_service.get_all_books()


        print(
            f"Database books: {len(all_books)}"
        )


        print("\nSample books:")

        for book in all_books[:5]:
            print(
                f"{book.title} | {book.price}"
            )


        # Export data
        export_service = ExportService()


        csv_file = export_service.export_csv(
            all_books
        )


        excel_file = export_service.export_excel(
            all_books
        )


        print("\nExport completed:")

        print(
            "CSV:",
            csv_file
        )

        print(
            "Excel:",
            excel_file
        )


    # Close database connections
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())