import logging
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.herodotus import handlers
from src.herodotus import logger

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            concurrent=True,
            stream=sys.stdout,
            level=logging.ERROR
        ),
        handlers.EnhancedFileHandler(
            filename="logs/test_log.log",
            concurrent=True,
            mode="a",
            encoding="utf-8",
            level=logging.WARNING
        )
    ]
)

lg.logger.warning("hello, world")
