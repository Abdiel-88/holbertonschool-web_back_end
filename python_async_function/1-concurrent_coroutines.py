#!/usr/bin/env python3
'''
Description: Import wait_random from
the previous python file that you’ve written
and write an async routine called wait_n that
takes in 2 int arguments: max_delay and n.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending
order without using sort() because of concurrency.
Arguments: n: int, max_delay: int = 10
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns wait_random n times with specified max_delay, returns the list of
    delays as they complete.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        completed_delays.append(delay)
    return completed_delays

if __name__ == "__main__":
    # Example usage:
    print(asyncio.run(wait_n(5, 10)))
    print(asyncio.run(wait_n(10, 10)))
    print(asyncio.run(wait_n(10, 0)))
