from abc import ABC, abstractmethod
from typing import Any


class BaseProvider(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get(item_name: str) -> Any:
        """Method to get the iteam value 
        
        Returns:
            None: If element has not been found
            Any: Iteam value if found
        """

        pass

class Singleton(type):

    _instance = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls is not None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance
