import logging
import os

DEFAULT_LOG_LEVEL  = "INFO"
DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s (%(threadName)s): %(message)s"


def create_path(file_path):
    """
    This function creates a path if it doesn't exist.

    :param file_path: Path for creation
    :return:
    """
    if not os.path.exists(file_path):
        path_without_filename = os.path.dirname(file_path)
        os.mkdir(path_without_filename)


def setup_logger(config):
    handlers = []
   
    if config.get("console_active", True):
        handlers.append(logging.StreamHandler())
    if config.get("file_active", True):
        file_path = config.get("file_path", "./log/default.log")
        create_path(file_path)
        handlers.append(logging.FileHandler(file_path))

    level = config.get("level", DEFAULT_LOG_LEVEL)
    format = config.get("format", DEFAULT_LOG_FORMAT)
    logging.basicConfig(level=level, format=format, handlers=handlers)