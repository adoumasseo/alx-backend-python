#!/usr/bin/env python3
'''7's module doc
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''return a tuple from string and integer
    '''
    return (k, float(v*v))
