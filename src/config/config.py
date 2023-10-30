import os
import json
from typing import Any
from platform import system

from base import BaseProvider, Singleton
from logger.logger import framework_logger


class OSConfigProvider(BaseProvider):

    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name, default=None)
        return value


class DictConfigProvider(BaseProvider):

    def __init__(self, conf_dict: dict) -> None:
        super().__init__()
        self.params = conf_dict

    def get(self, item_name: str) -> Any:
        if item_name in self.params:
            return self.params[item_name]
        return None
        

class JsonConfigProvider(BaseProvider):

    def __init__(self, config_path):
        self.params = self._read_config(config_path)

    @staticmethod
    def _read_config(config_path): 
        with open(config_path) as json_file:
            return json.load(json_file)    
    
    def get(self, item_name: str) -> Any:
        if item_name in self.params:
            return self.params[item_name]
        return None


class Config(metaclass=Singleton):   
    """Class responsible for storing framework's settings"""
    
    _conf_params = {}

    def __init__(self, conf_providers) -> None:
        self.conf_providers = conf_providers
        framework_logger.logger.debug(f"Providers added {', '.join(str(provider) for provider in self.conf_providers)}")

        #REGISTER PARAMETERS 
        self._register("DOMAIN")

        for param in self._conf_params:
            framework_logger.logger.info(f"Parameter '{param}' registered")


    def __getattr__(self, item_name: str):
        if item_name not in  self._conf_params:
            raise AttributeError(f"Please register '{item_name}' variable before usage")

        return self._conf_params[item_name]

    def _register(self, item_name: str):
        """
        Checks the providers in order - first one is the most significant and extracts the parameters.
        If parameter is found next providers are not checked.

        Raise: 
            AttributeError: If parameter is not found in provided data
        """
        for conf_provider in self.conf_providers:
            value = conf_provider.get(item_name)
            if value is not None:
                self._conf_params[item_name] = value
                framework_logger.logger.info(f"Got '{item_name}:{value}' parameter from {conf_provider}")
                return
            
        raise ValueError(f"{item_name} parameter is missing inside configuration providers")
            

conf_dict = {

}
    

if system() == "Windows":
    config = Config([JsonConfigProvider("src\\config\\env\\dev_config.json"), OSConfigProvider, DictConfigProvider(conf_dict)])
elif system() == "Linux":
    config = Config([JsonConfigProvider("src/config/env/dev_config.json"), OSConfigProvider, DictConfigProvider(conf_dict)])
else:
    raise Exception(f"No configuration for {system()} type OS")
