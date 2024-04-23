#!/usr/bin/env python3
'''
Description: Measures the total execution
time for wait_n from the previous file
and returns the average time per operation.
'''

import asyncio
import time
from typing import Callable, Coroutine, float
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of asynchronous
    tasks and compute the average time per task.

    Args:
    n (int): The number of tasks to run.
    max_delay (int): The maximum delay each task waits.

    Returns:
    float: The average time per task.
    """
    start_time = time.time()  # Start timing before the tasks start
    asyncio.run(wait_n(n, max_delay))  # Run the async tasks
    end_time = time.time()  # End timing after the tasks complete
    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return the average time per task


if __name__ == "__main__":
    # Example usage:
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))  # Prints the average time per operation
