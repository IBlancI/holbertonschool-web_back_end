#!/usr/bin/env python3
"""
Module containing the async_generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers asynchronously.
    Waits 1 second between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
