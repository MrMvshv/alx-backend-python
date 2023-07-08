#!/usr/bin/env python3
"""
Type annotated function that
takes a list of floats as argument
returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns a float that is the sum of the list elements"""
    return sum(input_list)
