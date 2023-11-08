import logging
import sys
from datetime import date
from typing import Any

from helpers.singleton import Singleton


class Logger(metaclass=Singleton):
    '''
    Logger wrapper class used for logging events accross the whole framework
    '''
    #change to the os.getpath + join
    _path = "logs//"
    _loggers = {}

    def __init__(self, name, log_file="logs.log", level=logging.INFO, level_stream=logging.WARNING) -> None:
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(message)s")
        
        self.file_handler = logging.FileHandler(filename=log_file + "_" + str(date.today()) + ".log", mode='a')
        self.file_handler.setLevel(level)
        self.file_handler.setFormatter(self.formatter)

        self.stream_handler = logging.StreamHandler(stream=sys.stderr)
        self.stream_handler.setLevel(level_stream)
        self.stream_handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(name)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
        self.logger.setLevel(min(level, level_stream))

        self._loggers[name] = level
        self.logger.debug(f"File handler level '{self.file_handler.level}'")
        self.logger.debug(f"Stream handler level '{self.stream_handler.level}'")
        self.logger.debug(f"Logger '{self.logger.name}' has been created and initialized")

    @classmethod
    def get_logger(self, name: str):
        if name not in self._loggers:
            raise AttributeError(f"No logger with '{name}' name has beed initialized")
        return logging.getLogger(name)
# DEFAULT LOGGER
Logger(name="framework", log_file=Logger._path + "framework", level=logging.DEBUG)

# CUSTOM LOGGERS
Logger(name="github_api_logger", log_file=Logger._path + "test_github_api", level=logging.DEBUG)
Logger(name="github_ui_logger", log_file=Logger._path + "test_github_ui", level=logging.DEBUG)

