#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time delay
    between 0 and max_delay seconds.

    Args:
    max_delay (int): The maximum delay time in seconds.

    Returns:
    float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    import asyncio
    wait_random = __import__('0-basic_async_syntax').wait_random
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
