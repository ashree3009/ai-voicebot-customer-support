from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="{time} | {level} | {message}",
    level="INFO"
)

logger.add(
    "voicebot.log",
    rotation="5 MB",
    retention="10 days"
)

def get_logger():
    return logger