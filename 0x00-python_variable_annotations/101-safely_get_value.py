#!/usr/bin/env python3
"""
Type-annotated function
return dct[key]
"""
from typing import TypeVar, Union, Mapping, Any



T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ returns the value or default(none)
    """
    if key in dct:
        return dct[key]
    else:
        return default
