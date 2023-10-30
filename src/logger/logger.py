import logging
import sys
from datetime import date


class Logger():
    '''
    Logger wrapper class used for logging events accross the whole framework
    '''
    path = "logs//"

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
        self.logger.setLevel(logging.DEBUG)

        self.logger.debug(f"File handler level '{self.file_handler.level}'")
        self.logger.debug(f"Stream handler level '{self.stream_handler.level}'")
        self.logger.debug(f"Logger '{self.logger.name}' has been created and initialized")

    def __del__(self):
        self.logger.debug(f"'{self.logger.name}' logger has beed destroyed")

# DEFAULT LOGGER
framework_logger = Logger(name="framework", log_file=Logger.path + "framework", level=logging.DEBUG)

# CUSTOM LOGGERS
github_api_logger = Logger(name="github_api_logger", log_file=Logger.path + "test_github_api", level=logging.DEBUG)