from typing import Any


class Singleton(type):

    _instance = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls is not None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance
