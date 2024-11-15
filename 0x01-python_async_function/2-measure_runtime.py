#!/usr/bin/env python3
'''module to measure an approximate elapsed time.'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''module to measure an approximate elapsed time.'''
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter() - start
    return float(end / n)
