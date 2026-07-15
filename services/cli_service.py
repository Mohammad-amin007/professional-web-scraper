from database import AsyncSessionLocal

from services.book_service import BookService
from services.analytics_service import AnalyticsService
from services.export_service import ExportService


class CLIService:


    async def show_analytics(self):

        async with AsyncSessionLocal() as session:

            book_service = BookService(
                session
            )

            books = await book_service.get_all_books()


            analytics = AnalyticsService()


            total = analytics.get_total_books(
                books
            )

            average = analytics.get_average_price(
                books
            )

            expensive = analytics.get_most_expensive_book(
                books
            )

            cheap = analytics.get_cheapest_book(
                books
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
                f"Most expensive: "
                f"{expensive.title} "
                f"(£{expensive.price:.2f})"
            )


            print(
                f"Cheapest: "
                f"{cheap.title} "
                f"(£{cheap.price:.2f})"
            )



    async def export_books(self):

        async with AsyncSessionLocal() as session:

            book_service = BookService(
                session
            )

            books = await book_service.get_all_books()


            export_service = ExportService()


            csv_file = export_service.export_csv(
                books
            )

            excel_file = export_service.export_excel(
                books
            )


            print("\nExport")
            print("-" * 60)


            print(
                f"CSV: {csv_file}"
            )


            print(
                f"Excel: {excel_file}"
            )