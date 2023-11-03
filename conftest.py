import pytest

from applications.github.api.github_api import GitHubAPI


@pytest.fixture(scope='session')
def github_api_app():
    #before each test 
    github_api_client = GitHubAPI()

    yield github_api_client

    #after each test executes: