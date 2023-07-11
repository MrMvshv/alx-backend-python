#!/usr/bin/env python3
""" function measure_runtime
    takes no arguments
    executes async_comprehension four times
    in parallel using asyncio.gather
"""
import time
import asyncio

import importlib.util

# Set the path to the module file
module_path = './1-async_comprehension.py'

# Load the module spec and create a module object
spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

# Execute the module to make its contents available
spec.loader.exec_module(module)

# Import the desired function from the module object
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime
       then return it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
