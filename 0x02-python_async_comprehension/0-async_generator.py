#!/usr/bin/env python3
'''first taks module'''
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Yield 10 times random float'''
    for i in range(10):
        yield random.random()
