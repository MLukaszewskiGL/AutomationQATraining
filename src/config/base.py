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
