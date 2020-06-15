"""
 Created by liwei on 2020/6/15.
"""
import asyncio, random


@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs)  # 通常yield from后都是接的耗时操作
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        # asyncio.sleep()是一个coroutine(里面也用了yield from)
        yield from asyncio.sleep(sleep_secs)  # 通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


loop = asyncio.get_event_loop()

tasks = [smart_fib(10), stupid_fib(10)]
# 通过事件循环来调度协程
loop.run_until_complete(asyncio.wait(tasks))

loop.close()
