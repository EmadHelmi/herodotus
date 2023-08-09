import logging
from sys import stdout

from herodotus import handlers
from herodotus import logger
from herodotus.utils import colorize

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=stdout,
            level=logging.ERROR,
            formatter=logging.Formatter(
                datefmt="%Y-%m-%dT%H:%M:%S",
                fmt="%(asctime)s | %(levelname)s: | %(message)s"
            )
        ),
        handlers.EnhancedFileHandler(
            filename="logs/test_log.log",
            mode="a",
            encoding="utf-8",
            level=logging.WARNING,
            formatter=logging.Formatter(
                datefmt="%Y-%m-%dT%H:%M:%S",
                fmt="%(asctime)s | %(message)s"
            )
        )
    ]
)

lg.logger.warning(colorize("Hello", foreground="green", styles=["bold", "underling"]))
