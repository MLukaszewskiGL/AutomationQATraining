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
* TBD

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
For each `Logger` instance the name of the logger needs to be provided - it allows to access this specific logger and it's configuration across the framework, file name which will store the logs and the logging level 
for the file storage and I/O stream.

**Example:**
```
logger = Logger(name=__name__,log_file=__name__, level=DEBUG)
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.debug("This is a debug message")
logger.info("This is an info message")
```
**2. Configuration**
* TBD

## Test module
Tests for the UI and API calls for GitHub

**1. Configuring and modifying**
* TBD
  
### Running tests
TBD

