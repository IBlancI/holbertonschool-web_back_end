#!/usr/bin/env python3
"""
Module containing the measure_runtime coroutine.
"""

import asyncio
import time
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time
