#!/usr/bin/env python3
""" coroutine async_generator
    takes no arguments.
"""
import random
import asyncio


async def async_generator():
    """loop 10 times, each time asynchronously wait 1 sec
       then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
