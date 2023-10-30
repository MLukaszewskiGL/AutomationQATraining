from logging import DEBUG,WARNING

from pytest import mark

from logger.logger import github_api_logger
from applications.github.api.github_api import GitHubAPI

logger = github_api_logger

@mark.github_api
class TestsGithubAPI():

    def test_for_existing_repo(self):
        logger.logger.info(f"Executing '{self.test_for_existing_repo.__name__}' test")

        github_api_client = GitHubAPI()
        existing_repo_name = 'AutomationQATraining'
        repos = github_api_client.search_repo(existing_repo_name)

        assert repos['total_count'] != 0

    def test_for_nonexisting_repo(self):
        logger.logger.info(f"Executing '{self.test_for_nonexisting_repo.__name__}' test")
        
        github_api_client = GitHubAPI()
        nonexisting_repo_name = 'nonoexistingrepo_name'
        repos = github_api_client.search_repo(nonexisting_repo_name)

        assert repos['total_count'] == 0
