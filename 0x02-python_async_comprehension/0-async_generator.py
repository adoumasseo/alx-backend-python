#!/usr/bin/env python3
'''first taks module'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Yield 10 times random float'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
