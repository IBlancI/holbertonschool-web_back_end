#!/usr/bin/env python3
"""
Module that provides a function to create a key-value pair tuple.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string and the second is the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple with the key and the square of the value.
    """
    return (k, float(v ** 2))