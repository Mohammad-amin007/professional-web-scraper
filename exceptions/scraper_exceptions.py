class ScraperException(Exception):
    """
    Base exception for scraper errors.
    """

    pass



class ScraperConnectionError(ScraperException):
    """
    Raised when connection to website fails.
    """

    pass



class ScraperTimeoutError(ScraperException):
    """
    Raised when website response takes too long.
    """

    pass



class ScraperHTTPError(ScraperException):
    """
    Raised when HTTP response status is not successful.
    """

    def __init__(
        self,
        status_code: int,
        message: str = "HTTP request failed"
    ):

        self.status_code = status_code

        super().__init__(
            f"{message}. Status code: {status_code}"
        )