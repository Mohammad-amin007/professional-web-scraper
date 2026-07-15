from unittest.mock import patch, Mock

from services.http_client import HttpClient



def test_http_client_success():


    fake_response = Mock()

    fake_response.ok = True

    fake_response.text = "test html"


    with patch(
        "services.http_client.requests.get",
        return_value=fake_response
    ):


        client = HttpClient()


        result = client.get(
            "https://example.com"
        )


        assert result == "test html"
import requests

from exceptions.scraper_exceptions import (
    ScraperTimeoutError,
)



def test_http_client_timeout():


    with patch(
        "services.http_client.requests.get",
        side_effect=requests.exceptions.Timeout
    ):


        client = HttpClient()


        try:

            client.get(
                "https://example.com"
            )

            assert False


        except ScraperTimeoutError:

            assert True