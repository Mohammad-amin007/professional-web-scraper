from bs4 import BeautifulSoup

from models.book import Book
from scrapers.base_scraper import BaseScraper


class ExampleScraper(BaseScraper):
    URL = "https://books.toscrape.com/"

    def run(self) -> list[Book]:
        html = self.fetch(self.URL)
        return self.parse(html)

    def parse(self, html: str) -> list[Book]:
        soup = BeautifulSoup(html, "lxml")

        books: list[Book] = []

        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"].strip()

            price_text = article.select_one(
                ".price_color"
            ).get_text(strip=True)

            # استخراج فقط اعداد و نقطه
            price = float(
                "".join(
                    char
                    for char in price_text
                    if char.isdigit() or char == "."
                )
            )

            books.append(
                Book(
                    title=title,
                    price=price,
                )
            )

        self.logger.info(
            f"{len(books)} books extracted."
        )

        return books