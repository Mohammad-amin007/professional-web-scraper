from models.book import Book
from services.analytics_service import AnalyticsService


def test_analytics():
    books = [
        Book(
            title="Book A",
            price=10,
            availability="In stock",
            rating=3,
            product_url="https://example.com/book-a",
        ),
        Book(
            title="Book B",
            price=20,
            availability="In stock",
            rating=4,
            product_url="https://example.com/book-b",
        ),
        Book(
            title="Book C",
            price=30,
            availability="Out of stock",
            rating=5,
            product_url="https://example.com/book-c",
        ),
    ]

    service = AnalyticsService()

    assert service.get_total_books(books) == 3
    assert service.get_average_price(books) == 20

    most_expensive = service.get_most_expensive_book(books)
    cheapest = service.get_cheapest_book(books)

    assert most_expensive is not None
    assert most_expensive.title == "Book C"

    assert cheapest is not None
    assert cheapest.title == "Book A"

    top_books = service.get_top_expensive_books(
        books,
        limit=2,
    )

    assert len(top_books) == 2
    assert top_books[0].title == "Book C"
    assert top_books[1].title == "Book B"