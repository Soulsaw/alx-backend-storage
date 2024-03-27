#!/usr/bin/env python3
"""Doc module"""
import redis
import uuid
from typing import Union
"""Import doc"""


class Cache:
    """Class well documented"""
    def __init__(self):
        """The default __init__ method"""
        self.__redis = redis.Redis()
        self.__redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that store the data"""
        key = uuid.uuid4()
        self.__redis.set(str(key), data)
        return str(key)
