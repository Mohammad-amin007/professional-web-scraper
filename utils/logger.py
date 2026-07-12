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

    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LoggerConfig.LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()