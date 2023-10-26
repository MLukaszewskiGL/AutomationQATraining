from logging import DEBUG,WARNING

from pytest import mark

from logger.logger import api_logger
from config.config import config

@mark.api
class TestsAPI():

    def test_dummy(self):
        api_logger.logger.info("Dummy info log")
        assert True
