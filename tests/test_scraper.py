from scrapers.example_scraper import (
    ExampleScraper,
)


def test_scraper_extracts_book_details():
    scraper = ExampleScraper()

    html = """
    <html>
        <body>

            <article class="product_pod">

                <p class="star-rating Four">
                    <i></i>
                </p>

                <h3>
                    <a
                        href="catalogue/test-book_1/index.html"
                        title="Test Book"
                    >
                        Test Book
                    </a>
                </h3>

                <p class="price_color">
                    £25.50
                </p>

                <p class="availability">
                    In stock
                </p>

            </article>

        </body>
    </html>
    """

    books = scraper.parse(
        html,
        page_url=(
            "https://books.toscrape.com/"
        ),
    )

    assert len(books) == 1

    book = books[0]

    assert book.title == "Test Book"
    assert book.price == 25.50
    assert book.availability == "In stock"
    assert book.rating == 4

    assert book.product_url == (
        "https://books.toscrape.com/"
        "catalogue/test-book_1/index.html"
    )


def test_scraper_skips_malformed_product():
    scraper = ExampleScraper()

    html = """
    <html>
        <body>
            <article class="product_pod">
                <h3>
                    <a title="Broken Book">
                        Broken Book
                    </a>
                </h3>
            </article>
        </body>
    </html>
    """

    books = scraper.parse(html)

    assert books == []

def test_scraper_extracts_next_page_url():
    scraper = ExampleScraper()

    html = """
    <html>
        <body>
            <ul class="pager">
                <li class="next">
                    <a href="page-2.html">
                        next
                    </a>
                </li>
            </ul>
        </body>
    </html>
    """

    next_url = scraper.get_next_page_url(
        html=html,
        page_url=(
            "https://books.toscrape.com/"
            "catalogue/page-1.html"
        ),
    )

    assert next_url == (
        "https://books.toscrape.com/"
        "catalogue/page-2.html"
    )


def test_scraper_returns_none_without_next_page():
    scraper = ExampleScraper()

    html = """
    <html>
        <body>
            <p>No more pages</p>
        </body>
    </html>
    """

    next_url = scraper.get_next_page_url(
        html=html,
        page_url=(
            "https://books.toscrape.com/"
            "catalogue/page-50.html"
        ),
    )

    assert next_url is None