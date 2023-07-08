#!/usr/bin/env python3
"""
Type annotated function to_kv
takes a string k and int or float v as args
returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple, 1st element of the tuple -> string k.
        2nd element is the square of the int/float v annotated as a float.
    """
    return k, float(v ** 2)
