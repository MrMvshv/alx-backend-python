#!/usr/bin/env python3
"""
Type annotated function sum_mixed_list
takes a list of ints and floats as argument
returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Returns a float that is the sum of the list elements"""
    return sum(mxd_lst)
