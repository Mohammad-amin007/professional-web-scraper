from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent


load_dotenv(
    BASE_DIR / ".env"
)



@dataclass(frozen=True)
class ScraperConfig:

    BASE_URL: str = os.getenv(
        "SCRAPER_BASE_URL",
        "https://books.toscrape.com/"
    )

    TIMEOUT: int = int(
        os.getenv(
            "SCRAPER_TIMEOUT",
            "15"
        )
    )

    RETRY_COUNT: int = int(
        os.getenv(
            "SCRAPER_RETRY_COUNT",
            "3"
        )
    )


    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )



@dataclass(frozen=True)
class StorageConfig:

    DATABASE = (
        BASE_DIR /
        "storage" /
        "scraper.db"
    )

    EXPORT_FOLDER = (
        BASE_DIR /
        "exports"
    )

    CSV_FOLDER = EXPORT_FOLDER

    EXCEL_FOLDER = EXPORT_FOLDER


@dataclass(frozen=True)
class LoggerConfig:

    LOG_FOLDER = (
        BASE_DIR /
        "logs"
    )


    LOG_FILE = (
        LOG_FOLDER /
        "scraper.log"
    )


    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )