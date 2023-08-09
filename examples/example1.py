import logging
from sys import stdout

from src.herodotus import EnhancedFileHandler
from src.herodotus import EnhancedStreamHandler
from src.herodotus import Logger
from src.herodotus import colorize, decolorize

test_logger = Logger(
    name="test_logger",
    level=logging.DEBUG,
    handlers=[
        EnhancedFileHandler(
            "logs/test_enhanced_file_handler.log",
            msg_func=decolorize
        ),
        EnhancedStreamHandler(
            stdout
        )
    ],
)

test_logger.logger.log(
    logging.DEBUG,
    f'{colorize("Hello", foreground="blue")} {colorize("W", foreground="green", styles=["bold", "italic"])}')
