from pathlib import Path

from models.book import Book
from services.export_service import ExportService


def create_books():
    return [
        Book(
            title="Book A",
            price=10.5,
            availability="In stock",
            rating=4,
            product_url="https://example.com/book-a",
        ),
        Book(
            title="Book B",
            price=20.5,
            availability="Out of stock",
            rating=5,
            product_url="https://example.com/book-b",
        ),
    ]


def test_export_csv(tmp_path):

    service = ExportService()

    service.export_folder = tmp_path

    file_path = service.export_csv(
        create_books()
    )

    assert file_path.exists()

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "Book A" in content
    assert "Book B" in content
    assert "product_url" in content



def test_export_json(tmp_path):

    service = ExportService()

    service.export_folder = tmp_path

    file_path = service.export_json(
        create_books()
    )

    assert file_path.exists()

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "Book A" in content
    assert "availability" in content
    assert "rating" in content



def test_export_excel(tmp_path):

    service = ExportService()

    service.export_folder = tmp_path

    file_path = service.export_excel(
        create_books()
    )

    assert file_path.exists()

    assert file_path.suffix == ".xlsx"