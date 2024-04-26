#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    """Generate random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
