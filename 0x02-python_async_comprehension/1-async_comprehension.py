#!/usr/bin/env python3
'''Use 0-async_generator'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Use async_generator and async comprehensing'''
    return [rFloat async for rFloat in async_generator()]
