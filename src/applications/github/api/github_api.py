import requests
import json

from logger.logger import Logger
from config.config import config

# Assign logger to it's alias
logger = Logger.get_logger("github_api_logger")

class GitHubAPI():
    """Class contains every API call we use in tests"""
    
    def __init__(self) -> None:
        pass
    

    def search_repo(self, repo_name: str):
        """
        Searches for the repository and returns the response body
        Documentation:
            https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
        Endpoint:
            config.DOMAIN/search/repositories
        Args:
            repo_name: str - name of the repository
        Returns:
            body: .json - body of the response
        """

        logger.debug(f"Sending request to https://api.github.com/search/repositories, params ='q': {repo_name}")

        # CHange /search/repos to contant and make separate file for this type of const like github_uris.json
        r = requests.get(config.DOMAIN + config.GIT_SEARCH_URI, params={'q': repo_name})
        
        body = r.json()
        logger.debug(f"Response body: {json.dumps(body,indent=4)}")
        return body
