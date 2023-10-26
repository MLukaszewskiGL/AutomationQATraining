import logging
import sys
from datetime import date

class Logger():
    '''
    Logger wrapper class used for logging events accross the whole framework
    '''

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

        self.logger.info(f"File handler level '{self.file_handler.level}'")
        self.logger.info(f"Stream handler level '{self.stream_handler.level}'")
        self.logger.info(f"Logger '{self.logger.name}' has been created and initialized")

    def __del__(self):
        self.logger.info(f"'{self.logger.name}' logger has beed destroyed")

# DEFAULT LOGGER
framework_logger = Logger(name="framework", log_file="framework", level=logging.DEBUG)

# CUSTOM LOGGERS
api_logger = Logger(name="api_logger", log_file="test_api", level=logging.INFO)