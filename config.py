from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).parent


@dataclass(frozen=True)
class ScraperConfig:
    BASE_URL: str = ""
    TIMEOUT: int = 15
    RETRY_COUNT: int = 3

    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )


@dataclass(frozen=True)
class StorageConfig:
    DATABASE = BASE_DIR / "storage" / "scraper.db"

    CSV_FOLDER = BASE_DIR / "exports"

    EXCEL_FOLDER = BASE_DIR / "exports"


@dataclass(frozen=True)
class LoggerConfig:
    LOG_FOLDER = BASE_DIR / "logs"

    LOG_FILE = LOG_FOLDER / "scraper.log"

    LOG_LEVEL = "INFO"