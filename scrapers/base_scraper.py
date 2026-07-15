from abc import ABC, abstractmethod

from services.http_client import HttpClient

from utils.logger import setup_logger



class BaseScraper(ABC):
    """
    Base class for all scrapers.
    """


    def __init__(self):

        self.logger = setup_logger()

        self.http_client = HttpClient()



    def fetch(
        self,
        url: str
    ) -> str:
        """
        Download page HTML using HttpClient.
        """


        self.logger.info(
            f"Fetching: {url}"
        )


        html = self.http_client.get(
            url
        )


        return html



    @abstractmethod
    def parse(
        self,
        html: str
    ):
        """
        Parse html.
        """

        pass