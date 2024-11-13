#!/usr/bin/env python3
'''Duck Type exercice'''
from typing import Any, Sequence, Union, List


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''None or lst[0]'''
    if lst:
        return lst[0]
    else:
        return None
