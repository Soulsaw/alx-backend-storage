#!/usr/bin/env python3
"""Doc module"""
import redis
import uuid
from typing import Union, Callable, Optional
"""Import doc"""


class Cache:
    """Class well documented"""
    def __init__(self):
        """The default __init__ method"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

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
