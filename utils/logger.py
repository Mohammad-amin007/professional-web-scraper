import logging
from pathlib import Path

from config import LoggerConfig


def setup_logger(name: str = "scraper") -> logging.Logger:
    """
    Create and configure application logger.
    """

    Path(LoggerConfig.LOG_FOLDER).mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(LoggerConfig.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LoggerConfig.LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger