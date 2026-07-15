from scrapers.example_scraper import ExampleScraper



def test_scraper_extracts_books():

    scraper = ExampleScraper()


    html = """
    <html>
        <body>

            <article class="product_pod">

                <h3>
                    <a title="Test Book">
                        Test Book
                    </a>
                </h3>


                <p class="price_color">
                    £25.50
                </p>

            </article>

        </body>
    </html>
    """


    books = scraper.parse(
        html
    )


    assert len(books) == 1


    assert books[0].title == "Test Book"


    assert books[0].price == 25.50