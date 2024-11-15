#!/usr/bin/env python3
'''Really don't know what to put now too lazy to think know'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Return a task from async'''
    return asyncio.create_task(wait_random(max_delay))
