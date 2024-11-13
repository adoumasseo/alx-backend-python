#!/usr/bin/env python3
'''8's Module'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''This function return the function below'''
    def fn(n: float) -> float:
        '''This function return a multiplication with multiplier'''
        return n * multiplier
    return fn
