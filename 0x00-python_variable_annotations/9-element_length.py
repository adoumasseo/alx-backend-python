#!/usr/bin/env python3
'''9's module'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''This return a list of tuple of sequence and int'''
    return [(i, len(i)) for i in lst]
