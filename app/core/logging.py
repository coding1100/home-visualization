import logging, sys
from loguru import logger

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = record.levelno
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())

def setup_logging():
    logging.getLogger().handlers = [InterceptHandler()]
    logger.remove()
    logger.add(sys.stderr, enqueue=True, backtrace=True, diagnose=False,
               level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
