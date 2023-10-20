import os


class Config():   
    """Class responsible for storing framework's and env's configuration"""

    request_timeout = 29
    user_name = os.environ.get('USERNAME')

    def __init__(self) -> None:
        pass
    
conf = Config()