import asyncio

import storage.models

from database import Base, AsyncSessionLocal, engine

from scrapers.example_scraper import ExampleScraper

from services.storage_service import StorageService
from services.book_service import BookService
from services.export_service import ExportService
from services.analytics_service import AnalyticsService

from utils.logger import logger



async def run_pipeline():

    logger.info(
        "Pipeline started"
    )

    try:

        async with engine.begin() as conn:

            await conn.run_sync(
                Base.metadata.create_all
            )


        logger.info(
            "Database initialized"
        )


        scraper = ExampleScraper()


        logger.info(
            "Scraper started"
        )


        books = scraper.run()


        logger.info(
            f"Extracted {len(books)} books"
        )



        async with AsyncSessionLocal() as session:


            storage_service = StorageService(
                session
            )


            await storage_service.save_books(
                books
            )


            logger.info(
                "Books saved successfully"
            )



            book_service = BookService(
                session
            )


            all_books = await book_service.get_all_books()


            logger.info(
                f"Loaded {len(all_books)} books from database"
            )



            analytics = AnalyticsService()



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



            print("\nSample books")
            print("-" * 60)


            for book in all_books[:5]:

                print(
                    f"{book.title} | £{book.price:.2f}"
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



            export_service = ExportService()


            csv_file = export_service.export_csv(
                all_books
            )


            excel_file = export_service.export_excel(
                all_books
            )

            json_file = export_service.export_json(
                all_books
            )



            print("\nExport")
            print("-" * 60)


            print(
                f"CSV: {csv_file}"
            )


            print(
                f"Excel: {excel_file}"
            )

            print(
                f"JSON: {json_file}"
            )



        logger.info(
            "Pipeline completed successfully"
        )


    except Exception:

        logger.exception(
            "Pipeline failed"
        )


    finally:

        await engine.dispose()




async def main():

    logger.info(
        "Application started"
    )

    await run_pipeline()



def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()