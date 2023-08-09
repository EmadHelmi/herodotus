import logging
from sys import stdout

from herodotus import handlers
from herodotus import logger

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
            level=logging.WARNING
        )
    ]
)

lg.logger.warning("hello, world")
