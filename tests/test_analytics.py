from models.book import Book

from services.analytics_service import AnalyticsService



def test_analytics():

    books = [

        Book(
            title="Book A",
            price=10
        ),

        Book(
            title="Book B",
            price=20
        ),

        Book(
            title="Book C",
            price=30
        ),

    ]


    analytics = AnalyticsService()


    assert analytics.get_total_books(
        books
    ) == 3


    assert analytics.get_average_price(
        books
    ) == 20


    expensive = analytics.get_most_expensive_book(
        books
    )

    assert expensive.title == "Book C"



    cheap = analytics.get_cheapest_book(
        books
    )

    assert cheap.title == "Book A"