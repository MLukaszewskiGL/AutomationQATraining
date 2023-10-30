# Automation QA Training

Trainig framework for testing GitHub API calls and UI.

# Framework structure 

##  Config module
### Description
Configuration parameters for the whole testing framework. Parameters can be stored in OS environment variables, python dictionary object and JSON file and can be accessed from all of them in one configuration.\
When the same parameter is defined in two or more configuration types (file, OS env. variable, dictionary) the order of the configuration types provided to the `config` variable are important, as after first definition of the parameter is found the value is returned. Order of the providers are defined when instance is initialized:
```
config = Config([JsonConfigProvider("path/to/config.json"), OSConfigProvider, DictConfigProvider(conf_dict)])
```
>**NOTE**
> Config class is implemented as Singleton

**1. Parameters description**
* DOMAIN - domain name of the tested endpoints

**2. How to modify and add parameters**\
Configuration parameters can be added/modified by editing:
* JSON file (`env` folder inside `config` directory)
* OS environmental variable e.g for Linux based distribution `export MY_PARAM=value`
* `conf_dict` dictionary inside `Config` class\
  
Then the parameter must be registered to be accessible in the framework, by adding `self._register("EXAMPLE_PARAM")` record below `#REGISTER PARAMETERS` comment inside `__init__` method of `Config` class. 

>**NOTE**
>All types of configuration type (file, OS env. variable, dictionary) can be accessed in one configuration. For more information go to the **Config module** description.  


**3. Accessing parameters**

* config module needs to be imported `from config import config`
* parameters can be accessed via call `config.PARAMETER_NAME` - if not found error will occur

## Application module
Module containing application to be tested with submodules for each feature.

**1. Submodules**
* API - submodule containig all API calls for the GitHub application.
* UI - submodule for UI 

## Helpers module 
Minor helper functions used by tests.

**1. How to add new methods**
 * TBD

## Logger module
Module used for the logging purposes of the tests execution steps and results.

**1. Usage**\
Logger class has been created as a wrapper for the `logging` python package with predefined configuration.  
For each `Logger` instance the name of the logger needs to be provided, file name which will store the logs and the logging level 
for the file storage and I/O stream.

**Example:**
```
logger = Logger(name=__name__,log_file=__name__, level=DEBUG)
logger.logger.warning("This is a warning message")
logger.logger.error("This is an error message")
logger.logger.debug("This is a debug message")
logger.logger.info("This is info message")
```
>**NOTE**
>By default the 'framework' logger is created. It's purpose is to gather logs from framework maintenance and configuration tasks. 

**2. Configuration**\
Adding new logger should take place in `logger/logger.py` file under `# CUSTOM LOGGERS` comment:
```
# CUSTOM LOGGERS
custom_logger = Logger(name="custom_logger", log_file="custom_logs", level=logging.INFO)
```
Then new custom logger should be imported in desired modul:
```
from logger.logger import custom_logger
```

## Test module
Tests for the UI and API calls for GitHub

**1. Configuring and modifying**
* TBD
  
### Running tests
TBD

