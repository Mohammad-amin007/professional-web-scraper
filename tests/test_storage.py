import pytest
from sqlalchemy import select

from models.book import Book
from services.storage_service import StorageService
from storage.models import BookModel


@pytest.mark.asyncio
async def test_save_book(
    test_session,
):
    service = StorageService(
        test_session
    )

    book = Book(
        title="Test Book",
        price=20.5,
        availability="In stock",
        rating=4,
        product_url=(
            "https://example.com/test-book"
        ),
    )

    await service.save_books(
        [book]
    )

    result = await test_session.execute(
        select(BookModel).where(
            BookModel.title == "Test Book"
        )
    )

    saved_book = (
        result.scalar_one_or_none()
    )

    assert saved_book is not None
    assert saved_book.title == "Test Book"
    assert saved_book.price == 20.5
    assert saved_book.availability == "In stock"
    assert saved_book.rating == 4

    assert saved_book.product_url == (
        "https://example.com/test-book"
    )