import logging
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.herodotus import handlers
from src.herodotus import logger
from src.herodotus.utils import colorize

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=sys.stdout,
            level=logging.WARNING,
            formatter=logging.Formatter(
                datefmt="%Y-%m-%dT%H:%M:%S",
                fmt="%(asctime)s | %(levelname)s | %(message)s"
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

lg.logger.warning(colorize("Hello", foreground="green", styles=["bold", "underline"]))
