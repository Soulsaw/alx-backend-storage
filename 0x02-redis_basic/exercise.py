#!/usr/bin/env python3
"""Doc module"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional
"""Import doc"""


def count_calls(method: Callable) -> Callable:
    """Create and return a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """The callable method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """The callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """# Initialize Redis client"""

        # Create keys for input and output lists
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Append input arguments to the input list
        self._redis.rpush(input_key, str(args))

        # Execute the original method to retrieve the output
        output = method(self, *args, **kwargs)

        # Append the output to the output list
        self._redis.rpush(output_key, output)

        return output
    return wrapper


class Cache:
    """Class well documented"""
    def __init__(self):
        """The default __init__ method"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> bytes:
        """Get methods implem"""
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> str:
        """Return a str"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Return a str"""
        return self.get(key, int)
