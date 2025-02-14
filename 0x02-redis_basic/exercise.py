#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method
    Module
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A Count Calls Decorator function takes a single method
        callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ A Wrapper function that increments the count for
            that key every time the method is called
        """
        self._redis.incr(key)
        return (method(self, *args, **kwargs))

    return (wrapper)


def call_history(method: Callable) -> Callable:
    """ A Call History Decorator function that stores the history
        of inputs and outputs for a particular function
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper Function """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return (result)

    return (wrapper)


def replay(method: Callable) -> None:
    """ A Replay Function to display the history
        of calls of a particular function.
    """
    r = redis.Redis()
    method_name = method.__qualname__

    inputs_key = method_name + ":inputs"
    outputs_key = method_name + ":outputs"

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for input, output in zip(inputs, outputs):
        print(f"{method_name}(*{eval(input)}) -> {output}")


class Cache:
    """ Cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A store method """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return (random_key)

    def get(self, key: str, fn: Callable = None):
        """A get method """
        data = self._redis.get(str(key))
        if fn:
            data = fn(data)

        return (data)

    def get_str(self, key: str) -> str:
        """ A get_Str method"""
        return (self.get(key, fn=lambda x: x.decode("utf-8")))

    def get_int(self, key: str) -> int:
        """ A get_int method """
        return (self.get(key, int))
