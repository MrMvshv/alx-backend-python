#!/usr/bin/env python3
"""
Duck-type annotated function
takes a list
returns first element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns first element of list
    """
    if lst:
        return lst[0]
    else:
        return None
