
import logging
from typing import Union


def initialize_logging(level: Union[int, str] = logging.INFO) -> None:
    """Initializes logger.

    Args:
        level: Logging level to use. Defaults to logging.DEBUG.
    """
    if type(level) == str:
        level = logging.getLevelName(level.upper())

    # shorter log level name for better alignment
    logging.addLevelName(logging.CRITICAL, "CRT")
    logging.addLevelName(logging.ERROR, "ERR")
    logging.addLevelName(logging.WARNING, "WRN")
    logging.addLevelName(logging.INFO, "INF")
    logging.addLevelName(logging.DEBUG, "DBG")

    # create logger
    logging.basicConfig(level=level, format="[%(asctime)s] [%(levelname)-3s] [%(filename)s:%(lineno)s] %(message)s")

if __name__ == "__main__":
    initialize_logging("INFO")
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning.")
    logging.error("This is an error.")
