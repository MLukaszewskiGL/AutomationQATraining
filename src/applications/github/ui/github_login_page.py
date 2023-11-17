import hashlib

from selenium.webdriver.common.by import By

from config.config import config
from logger.logger import Logger
from base_page import BasePage
from helpers.browser_provider import BrowserProvider


logger = Logger.get_logger("github_ui_logger")


class GithubLoginPage(BasePage):
    """Github login page object
    
    Methods:
        TBD
    """
    

    def __init__(self, browser_name) -> None:
        """Initialize the proper driver corresponding to the defined one in config.BROWSER parameter"""
        self.driver = BrowserProvider.get_driver(browser_name)
    def navigate_to_page(self) -> None:
        "Navigates to config.GIT_LOGIN_PAGE uri defined in config files"

        self.driver.get(config.GIT_LOGIN_PAGE)
        # add logging

    def find_el(self, locator_name, locator_value):
        # add waiters / checks
        # return found element
        # replace driver.find_element method :)
        pass


    def try_to_login(self, username: str, password: str) -> None:
        """Tryes to login into the github account 
        
        Args:
            username: str - account's username 
            password: str - account's password
        """

        logger.debug(f"Logging into github using username: {username}")
        login_fld = self.driver.find_element(By.ID ,"login_field")
        login_fld.send_keys(username)
        
        hash_passwd = hashlib.sha256(password.encode('utf-8')).digest()
        logger.debug(f"Logging into github using password: {hash_passwd}")
        pass_fld = self.driver.find_element(By.ID ,"password") 
        pass_fld.send_keys(password)

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
    