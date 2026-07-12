import asyncio

import storage.models

from database import Base, AsyncSessionLocal, engine

from scrapers.example_scraper import ExampleScraper

from services.storage_service import StorageService
from services.book_service import BookService
from services.export_service import ExportService
from services.analytics_service import AnalyticsService

from utils.logger import logger


async def main():

    logger.info("Application started")

    try:

        # Create database tables
        async with engine.begin() as conn:
            await conn.run_sync(
                Base.metadata.create_all
            )

        logger.info("Database initialized")


        # Run scraper
        scraper = ExampleScraper()

        logger.info("Scraper started")

        books = scraper.run()

        logger.info(
            f"Extracted {len(books)} books"
        )


        async with AsyncSessionLocal() as session:


            # Save books
            storage_service = StorageService(session)

            await storage_service.save_books(
                books
            )

            logger.info(
                "Books saved successfully"
            )


            # Read books
            book_service = BookService(session)

            all_books = await book_service.get_all_books()

            logger.info(
                f"Loaded {len(all_books)} books from database"
            )


            print("\nSample books")
            print("-" * 60)

            for book in all_books[:5]:
                print(
                    f"{book.title} | £{book.price:.2f}"
                )


            # Analytics
            analytics = AnalyticsService()

            logger.info(
                "Analytics started"
            )


            total = analytics.get_total_books(
                all_books
            )

            average = analytics.get_average_price(
                all_books
            )

            expensive = analytics.get_most_expensive_book(
                all_books
            )

            cheap = analytics.get_cheapest_book(
                all_books
            )


            logger.info(
                f"Total books: {total}"
            )

            logger.info(
                f"Average price: {average}"
            )

            logger.info(
                f"Most expensive: {expensive.title}"
            )

            logger.info(
                f"Cheapest: {cheap.title}"
            )


            print("\nAnalytics")
            print("-" * 60)

            print(
                f"Total books: {total}"
            )

            print(
                f"Average price: £{average:.2f}"
            )

            print(
                f"Most expensive: {expensive.title} (£{expensive.price:.2f})"
            )

            print(
                f"Cheapest: {cheap.title} (£{cheap.price:.2f})"
            )


            # Export
            export_service = ExportService()

            csv_file = export_service.export_csv(
                all_books
            )

            excel_file = export_service.export_excel(
                all_books
            )


            logger.info(
                "CSV export completed"
            )

            logger.info(
                "Excel export completed"
            )


            print("\nExport")
            print("-" * 60)

            print(
                f"CSV: {csv_file}"
            )

            print(
                f"Excel: {excel_file}"
            )


        logger.info(
            "Application finished successfully"
        )


    except Exception:

        logger.exception(
            "Application failed"
        )


    finally:

        await engine.dispose()



if __name__ == "__main__":
    asyncio.run(main())