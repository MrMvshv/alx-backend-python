#!/usr/bin/env python3
""" async func , takes int arg default value 10 wait_random
    waits for a random delay between 0 and max_delay seconds
    eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that waits
       then return the value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
