#!/usr/bin/env python3
"""
Redis basic exercise
"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method of the Cache class is called.
    Uses the method's qualified name as the Redis key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    for a particular function in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store inputs
        self._redis.rpush(input_key, str(args))

        # Execute function
        result = method(self, *args, **kwargs)

        # Store outputs
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(
            f"{method_name}(*{inp.decode('utf-8')}) -> "
            f"{out.decode('utf-8')}"
        )


class Cache:
    """Cache class using Redis"""

    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random UUID key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        Preserves the original Redis.get behavior (returns None) if key does
        not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a string value from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer value from Redis."""
        return self.get(key, fn=int)
