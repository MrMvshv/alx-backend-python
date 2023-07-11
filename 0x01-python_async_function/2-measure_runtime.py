#!/usr/bin/env python3
""" measures execution time
    for wait_n and returns total_time/n
    as a float
"""
from typing import List
import time
import asyncio

import importlib.util

# Set the path to the module file
module_path = './1-concurrent_coroutines.py'

# Load the module spec and create a module object
spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

# Execute the module to make its contents available
spec.loader.exec_module(module)

# Import the desired function from the module object
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns sorted lists containing
       max_delay random values
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
