import time

import requests

from config import ScraperConfig

from exceptions.scraper_exceptions import (
    ScraperConnectionError,
    ScraperTimeoutError,
    ScraperHTTPError,
)

from utils.logger import logger



class HttpClient:


    def get(
        self,
        url: str
    ) -> str:


        last_exception = None


        for attempt in range(
            1,
            ScraperConfig.RETRY_COUNT + 1
        ):


            try:

                logger.info(
                    f"HTTP GET: {url} (Attempt {attempt})"
                )


                response = requests.get(
                    url,
                    headers={
                        "User-Agent":
                        ScraperConfig.USER_AGENT
                    },
                    timeout=ScraperConfig.TIMEOUT
                )


                if not response.ok:

                    raise ScraperHTTPError(
                        response.status_code
                    )


                logger.info(
                    "HTTP request successful."
                )


                return response.text



            except requests.exceptions.Timeout as exc:

                last_exception = ScraperTimeoutError(
                    "Website response timeout"
                )


                logger.warning(
                    f"Timeout error. Attempt {attempt}"
                )



            except requests.exceptions.ConnectionError as exc:

                last_exception = ScraperConnectionError(
                    "Connection to website failed"
                )


                logger.warning(
                    f"Connection error. Attempt {attempt}"
                )



            except ScraperHTTPError as exc:

                last_exception = exc


                logger.warning(
                    str(exc)
                )



            except requests.RequestException as exc:

                last_exception = exc


                logger.warning(
                    f"Unexpected HTTP error: {exc}"
                )



            if attempt < ScraperConfig.RETRY_COUNT:

                wait_time = attempt * 2


                logger.info(
                    f"Retrying in {wait_time} seconds..."
                )


                time.sleep(
                    wait_time
                )



        logger.exception(
            "HTTP request failed after all retries."
        )


        raise last_exception