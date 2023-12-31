import pytest

from applications.github.api.github_api import GitHubAPI
from applications.github.ui.github_login_page import GithubLoginPage
from config.config import config

@pytest.fixture(scope='session')
def github_api_app():
    """Fixture for creating class containing API calls"""

    github_api_client = GitHubAPI()

    yield github_api_client
    
@pytest.fixture()
def github_login_page():
    """Login page object fixture for generating the login page object"""

    github_login_page = GithubLoginPage(config.BROWSER)
    github_login_page.navigate_to_page()

    yield github_login_page

    github_login_page.close_browser()
