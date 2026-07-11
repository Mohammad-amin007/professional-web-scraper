from abc import ABC, abstractmethod

import requests
from requests import Response

from config import ScraperConfig
from utils.logger import setup_logger


class BaseScraper(ABC):
    """
    Base class for all scrapers.
    """

    def __init__(self):
        self.logger = setup_logger()

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": ScraperConfig.USER_AGENT
            }
        )

    def fetch(self, url: str) -> str:
        """
        Download page HTML.
        """

        self.logger.info(f"Fetching: {url}")

        response: Response = self.session.get(
            url,
            timeout=ScraperConfig.TIMEOUT
        )

        response.raise_for_status()

        self.logger.info("Page downloaded successfully.")

        return response.text

    @abstractmethod
    def parse(self, html: str):
        """
        Parse html.
        """
        pass