#!/usr/bin/env python3
"""
Description: Write a coroutine called async_generator that takes no arguments.
             The coroutine will loop 10 times, each time asynchronously wait
             1 second, then yield a random number between 0 and 10. Use the
             random module.
"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator yielding a random float between 0 and 10,
    once per second, for 10 seconds.
    """
    for _ in range(10):
        await sleep(1)  # Asynchronous wait for 1 second
        yield uniform(0, 10)  # Yield a random float between 0 and 10


# Function to test the generator
async def print_yielded_values():
    result = []
    async for value in async_generator():
        result.append(value)
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(print_yielded_values())
