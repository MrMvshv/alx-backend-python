#!/usr/bin/env python3
""" function async_comprehension
    takes no arguments
    returns 10 random numbers
"""
from typing import List
import asyncio

import importlib.util

# Set the path to the module file
module_path = './0-async_generator.py'

# Load the module spec and create a module object
spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

# Execute the module to make its contents available
spec.loader.exec_module(module)

# Import the desired function from the module object
async_generator = module.async_generator


async def async_comprehension():
    """using an async comprehensing over async_generator
       then return the 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
