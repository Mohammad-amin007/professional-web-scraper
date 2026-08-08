from urllib.parse import urljoin

from bs4 import BeautifulSoup

from config import ScraperConfig
from models.book import Book
from scrapers.base_scraper import BaseScraper
from utils.logger import logger


class ExampleScraper(BaseScraper):
    URL = ScraperConfig.BASE_URL

    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    def run(self) -> list[Book]:
        logger.info(
            f"Starting scraper: {self.URL}"
        )

        books: list[Book] = []
        current_url: str | None = self.URL

        visited_urls: set[str] = set()
        page_number = 1

        try:
            while current_url:
                if current_url in visited_urls:
                    logger.warning(
                        f"Pagination loop detected: {current_url}"
                    )
                    break

                visited_urls.add(current_url)

                logger.info(
                    f"Scraping page {page_number}: "
                    f"{current_url}"
                )

                html = self.fetch(current_url)

                page_books = self.parse(
                    html=html,
                    page_url=current_url,
                )

                books.extend(page_books)

                logger.info(
                    f"Page {page_number} completed. "
                    f"Extracted {len(page_books)} books."
                )

                current_url = self.get_next_page_url(
                    html=html,
                    page_url=current_url,
                )

                page_number += 1

            logger.info(
                f"Scraper finished. "
                f"Total extracted books: {len(books)}"
            )

            return books

        except Exception:
            logger.exception(
                "Scraper failed."
            )

            return books

    def parse(
        self,
        html: str,
        page_url: str | None = None,
    ) -> list[Book]:
        try:
            soup = BeautifulSoup(
                html,
                "lxml",
            )

            books: list[Book] = []

            base_url = page_url or self.URL

            for article in soup.select(
                "article.product_pod"
            ):
                title_element = article.select_one(
                    "h3 a"
                )

                price_element = article.select_one(
                    ".price_color"
                )

                availability_element = (
                    article.select_one(
                        ".availability"
                    )
                )

                rating_element = (
                    article.select_one(
                        "p.star-rating"
                    )
                )

                if (
                    title_element is None
                    or price_element is None
                ):
                    logger.warning(
                        "Skipping malformed product."
                    )
                    continue

                title = (
                    title_element
                    .get("title", "")
                    .strip()
                )

                if not title:
                    logger.warning(
                        "Skipping product without title."
                    )
                    continue

                price_text = (
                    price_element
                    .get_text(strip=True)
                )

                numeric_price = "".join(
                    char
                    for char in price_text
                    if char.isdigit()
                    or char == "."
                )

                if not numeric_price:
                    logger.warning(
                        f"Skipping product with invalid price: "
                        f"{title}"
                    )
                    continue

                price = float(
                    numeric_price
                )

                availability = (
                    availability_element
                    .get_text(
                        " ",
                        strip=True,
                    )
                    if availability_element
                    else "Unknown"
                )

                rating = self._extract_rating(
                    rating_element
                )

                href = title_element.get(
                    "href",
                    "",
                )

                product_url = urljoin(
                    base_url,
                    href,
                )

                books.append(
                    Book(
                        title=title,
                        price=price,
                        availability=availability,
                        rating=rating,
                        product_url=product_url,
                    )
                )

            logger.info(
                f"{len(books)} books extracted "
                f"from page."
            )

            return books

        except Exception:
            logger.exception(
                "Parsing failed."
            )

            return []

    def get_next_page_url(
        self,
        html: str,
        page_url: str,
    ) -> str | None:
        soup = BeautifulSoup(
            html,
            "lxml",
        )

        next_link = soup.select_one(
            "li.next a"
        )

        if next_link is None:
            return None

        href = next_link.get(
            "href"
        )

        if not href:
            return None

        return urljoin(
            page_url,
            href,
        )

    def _extract_rating(
        self,
        rating_element,
    ) -> int:
        if rating_element is None:
            return 0

        classes = rating_element.get(
            "class",
            [],
        )

        for class_name in classes:
            rating = self.RATING_MAP.get(
                class_name
            )

            if rating is not None:
                return rating

        return 0