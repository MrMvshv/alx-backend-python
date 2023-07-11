#!/usr/bin/env python3
""" async routine, takes 2 int arg n andd max_delay
    spawns wait_random n times with
    the specified max_delay.
"""
from typing import List
import asyncio

import importlib.util

# Set the path to the module file
module_path = './3-tasks.py'

# Load the module spec and create a module object
spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

# Execute the module to make its contents available
spec.loader.exec_module(module)

# Import the desired function from the module object
task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns sorted lists containing
       max_delay random values
    """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = []
    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
