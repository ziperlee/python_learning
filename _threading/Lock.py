"""
 Create by zipee on 2019/1/5.
"""
from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import ctime, sleep

import click

__author__ = 'zipee'

loops = [randrange(2, 5) for x in range(randrange(3, 7))]
remaining = set()
lock = Lock()

def loop(nsec):
    thread_name = current_thread().name
    remaining.add(thread_name)
    print(f"start thread-{thread_name} at: {ctime()}")
    sleep(nsec)
    remaining.remove(thread_name)
    print(f"thread-{thread_name} is completed at: {ctime()}")
    print(f"remaining: {remaining or 'NONE'}")

def loop2(nsec):
    thread_name = current_thread().name
    lock.acquire()
    # lock.acquire()
    remaining.add(thread_name)
    print(f"start thread-{thread_name} at: {ctime()}")
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(thread_name)
    print(f"thread-{thread_name} is completed at: {ctime()}")
    print(f"remaining: {remaining or 'NONE'}")
    lock.release()

def loop3(nsec):
    thread_name = current_thread().name
    with lock:
        remaining.add(thread_name)
        print(f"start thread-{thread_name} at: {ctime()}")
    sleep(nsec)
    with lock:
        remaining.remove(thread_name)
        print(f"thread-{thread_name} is completed at: {ctime()}")
        print(f"remaining: {remaining or 'NONE'}")


@click.group()
def main():
    pass

@main.command()
# 不加锁，运行结果可能会乱
def main1():
    threads = []
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@main.command()
# 加锁，运行结果如预期
def main2():
    threads = []
    for pause in loops:
        Thread(target=loop2, args=(pause,)).start()

@main.command()
# 使用with（上下文管理）进行加锁
def main3():
    threads = []
    for pause in loops:
        Thread(target=loop3, args=(pause,)).start()



@register
def _atexit():
    print(f"all done at: {ctime()}")

if __name__ == "__main__":
    main()