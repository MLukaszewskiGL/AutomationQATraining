import logging
import sys
from datetime import date

class Logger():
    '''
    Logger wrapper class used for logging events accross the whole framework
    '''

    def __init__(self, name, log_file="logs.log", level=logging.INFO, level_stream=logging.WARNING) -> None:
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(message)s")
        
        self.file_handler = logging.FileHandler(filename=log_file + "_" + str(date.today()) + ".log", mode='w')
        self.file_handler.setLevel(level)
        self.file_handler.setFormatter(self.formatter)

        self.stream_handler = logging.StreamHandler(stream=sys.stderr)
        self.stream_handler.setLevel(level_stream)
        self.stream_handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(name)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(f"Logger {name} has been created and initialized")

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
    
    def criticar(self, message):
        self.logger.critical(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def info(self, message):
        self.logger.info(message)


