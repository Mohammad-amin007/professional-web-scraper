from bs4 import BeautifulSoup

from models.book import Book
from scrapers.base_scraper import BaseScraper

from config import ScraperConfig
from utils.logger import logger


class ExampleScraper(BaseScraper):

    URL = ScraperConfig.BASE_URL

    def run(self) -> list[Book]:

        logger.info(
            f"Starting scraper: {self.URL}"
        )

        try:
            html = self.fetch(self.URL)

            logger.info(
                "Page downloaded successfully."
            )

            books = self.parse(html)

            logger.info(
                f"Scraper finished. Extracted {len(books)} books."
            )

            return books

        except Exception:

            logger.exception(
                "Scraper failed."
            )

            return []


    def parse(self, html: str) -> list[Book]:

        try:

            soup = BeautifulSoup(
                html,
                "lxml"
            )

            books: list[Book] = []


            for article in soup.select(
                "article.product_pod"
            ):

                title = (
                    article
                    .h3
                    .a["title"]
                    .strip()
                )


                price_text = (
                    article
                    .select_one(".price_color")
                    .get_text(strip=True)
                )


                price = float(
                    "".join(
                        char
                        for char in price_text
                        if char.isdigit()
                        or char == "."
                    )
                )


                books.append(
                    Book(
                        title=title,
                        price=price,
                    )
                )


            logger.info(
                f"{len(books)} books extracted."
            )


            return books


        except Exception:

            logger.exception(
                "Parsing failed."
            )

            return []