#!/usr/bin/env python3
"""
Module that provides a function to calculate the lengths of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing the elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element and its length.
    """
    return [(i, len(i)) for i in lst]