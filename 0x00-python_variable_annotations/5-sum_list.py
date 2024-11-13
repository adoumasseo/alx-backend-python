#!/usr/bin/env python3
"""Sum of list element but with annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Take a list and return the sum of his elt"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
