#!/usr/bin/env python3
''' Description: Write a coroutine called async_comprehension that takes no
                 arguments.
                 The coroutine will collect 10 random numbers using an async
                 comprehensing over async_generator, then return the 10 random
                 numbers.
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of values from async_generator"""
    return [i async for i in async_generator()]
