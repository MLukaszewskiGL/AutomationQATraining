from selenium import webdriver

from logger.logger import Logger
from config.config import config

logger = Logger.get_logger("github_ui_logger")


class BrowserProvider():

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_driver(browser_name):

        if browser_name == "chrome":
            logger.debug("Chrome browser selected")
            driver = webdriver.Chrome()
        else:
            logger.error(f"Non existing browser ({config.BROWSER}) has been selected")
            raise ValueError("Non existing browser has been selected")
        
        return driver
    