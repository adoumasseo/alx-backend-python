#!/usr/bin/env python3
'''This is about learning how to use asyncio'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''This is about learning how to use asyncio'''
    wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
        )
    return sorted(wait_times)
