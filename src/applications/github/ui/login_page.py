import hashlib

from selenium import webdriver
from selenium.webdriver.common.by import By

from config.config import config
from logger.logger import Logger


logger = Logger.get_logger("github_ui_logger")

class GitHubUILoginPage():
    """Github login page object
    
    Methods:

    """
    

    def __init__(self) -> None:
        """Initialize the proper driver corresponding to the defined one in config.BROWSER parameter"""

        if config.BROWSER == "chrome":
            logger.debug("Chrome browser selected")
            self.driver = webdriver.Chrome()
        else:
            logger.error(f"Non existing browser ({config.BROWSER}) has been selected")
            raise ValueError("Non existing browser has been selected")

    def navigate_to_page(self) -> None:
        "Navigates to config.GIT_LOGIN_PAGE uri defined in config files"

        self.driver.get(config.GIT_LOGIN_PAGE)
        # add logging

    def try_to_login(self, username: str, password: str) -> None:
        """Tryes to login into the github account 
        
        Args:
            username: str - account's username 
            password: str - account's password
        """

        login_fld = self.driver.find_element(By.ID ,"login_field")
        login_fld.send_keys(username)
        logger.debug(f"Logging into github using username: {username}")

        pass_fld = self.driver.find_element(By.ID ,"password") 
        pass_fld.send_keys(password)
        logger.debug(f"Logging into github using password: {hashlib.sha256(password.encode('utf-8')).digest()}")

        login_fld = self.driver.find_element(By.NAME ,"commit")
        login_fld.click()

    def check_error_message(self) -> bool:
        """Checks if the output message of logging is ERROR or not"""

        error_msg = self.driver.find_element(By.ID ,"js-flash-container")
        logger.debug(f"Error message: {error_msg}")
        
        return error_msg is not None
    
    def close_browser(self) -> None:
        """Close initialized browser"""
        
        self.driver.quit()
    