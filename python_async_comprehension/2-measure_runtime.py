#!/usr/bin/env python3
"""
This script demonstrates the use of async comprehensions in Python.
It defines a coroutine function that collects
random numbers using an async comprehension.
"""
import asyncio
from typing import List
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
