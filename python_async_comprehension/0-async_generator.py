import asyncio
import random

async def async_generator():
    """
    Asynchronous generator that yields random integers between 0 and 10.

    This generator uses the `asyncio.sleep()` function to introduce a delay of 1 second
    between each yield. It generates a total of 10 random integers.

    Yields:
        int: A random integer between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)