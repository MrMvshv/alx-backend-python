#!/usr/bin/env python3
""" function measure_runtime
    takes no arguments
    executes async_comprehension four times
    in parallel using asyncio.gather
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime
       then return it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
