#!/usr/bin/env python3
"""
Type annotated function element_length
takes a list
returns a list of tuples
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a function that multiplies a float by multiplier.
    """
    return [(i, len(i)) for i in lst]
