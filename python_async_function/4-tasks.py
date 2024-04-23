#!/usr/bin/env python3
'''
Description: Function to execute multiple wait_random tasks concurrently and
return the list of all the delays (float values).
'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n tasks that execute wait_random
    concurrently and returns a list of delays.

    Args:
    n (int): Number of tasks to spawn.
    max_delay (int): Maximum delay to pass to wait_random.

    Returns:
    List[float]: List of float values representing the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

if __name__ == "__main__":
    # This part is just for local testing.
    import asyncio
    task_wait_n = __import__('4-tasks').task_wait_n
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
