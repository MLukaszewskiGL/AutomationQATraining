from logging import DEBUG,WARNING

from logger.logger import Logger
from config.config import conf



def test_logger():
    logger = Logger(name=__name__,log_file=__name__, level=DEBUG)
    logger.warning("This is a warning")
    logger.error("This is a error")
    logger.debug("This is a debug")
    logger.info("This is a info")
    assert True

def test_config():
    print(conf.request_timeout)