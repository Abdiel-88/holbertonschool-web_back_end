#!/usr/bin/env python3
'''
Description: Function to create an asyncio.Task from a coroutine.
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task to execute the wait_random coroutine.

    Args:
    max_delay (int): Maximum delay to pass to wait_random coroutine.

    Returns:
    asyncio.Task: The created task that will run the wait_random coroutine.
    """
    # Create a task from the wait_random coroutine
    task = asyncio.create_task(wait_random(max_delay))
    return task


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)  # Should print <class '_asyncio.Task'>

    asyncio.run(test(5))
