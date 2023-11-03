import pytest
from pytest import mark

from logger.logger import Logger
from applications.github.api.github_api import GitHubAPI


logger = Logger.get_logger("github_api_logger")

@mark.github_api
class TestsGithubAPI():

    def test_for_existing_repo(self, github_api_app):
        existing_repo_name = 'AutomationQATraining'
        repos = github_api_app.search_repo(existing_repo_name)

        assert repos['total_count'] != 0

    def test_for_nonexisting_repo(self,github_api_app):
        nonexisting_repo_name = 'nonoexistingrepo_name'
        repos = github_api_app.search_repo(nonexisting_repo_name)

        assert repos['total_count'] == 0
