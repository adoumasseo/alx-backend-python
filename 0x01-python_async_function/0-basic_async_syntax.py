#!/usr/bin/env python3
'''First module using asyncio'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Here we use asyncio to simulate a wait'''
    randValue: float = random.uniform(0, max_delay)
    await asyncio.sleep(randValue)
    return randValue
