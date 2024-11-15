#!/usr/bin/env python3
'''11's module'''
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Return Any or None'''
    if key in dct:
        return dct[key]
    else:
        return default
