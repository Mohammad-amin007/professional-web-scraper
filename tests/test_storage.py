import pytest

from sqlalchemy import select

from models.book import Book

from storage.models import BookModel

from services.storage_service import StorageService



@pytest.mark.asyncio
async def test_save_book(
    test_session
):

    service = StorageService(
        test_session
    )


    book = Book(
        title="Test Book",
        price=20.5
    )


    await service.save_books(
        [
            book
        ]
    )


    result = await test_session.execute(
        select(BookModel)
    )


    books = result.scalars().all()


    assert len(books) == 1


    assert books[0].title == "Test Book"


    assert books[0].price == 20.5