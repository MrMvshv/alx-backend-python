#!/usr/bin/env python3
""" function task_wait_random
    takes an integer max_delay
    returns a asyncio.Task.
"""
from typing import List
import asyncio

import importlib.util

# Set the path to the module file
module_path = './0-basic_async_syntax.py'

# Load the module spec and create a module object
spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

# Execute the module to make its contents available
spec.loader.exec_module(module)

# Import the desired function from the module object
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio.Task
       takes an int
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
