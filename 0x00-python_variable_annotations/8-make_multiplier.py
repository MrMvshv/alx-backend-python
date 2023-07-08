#!/usr/bin/env python3
"""
Type annotated function make_multiplier
takes a float multiplier
returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(num: float) -> float:
        """Multiplier function to be returned"""
        return num * multiplier

    return multiplier_function
