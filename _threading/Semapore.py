"""
 Create by zipee on 2019/1/5.
"""
__author__ = 'zipee'

from threading import Semaphore, BoundedSemaphore
# 信号量设置为1的时候就是锁，Lock

# Semaphore 可以超出acquire次数的调用
sema = Semaphore(1)

sema.acquire()

sema.release()

sema.release()

with sema:
    print('use sema in with')

# BoundedSemaphore 不可以超出acquire次数的调用
bsema = BoundedSemaphore(1)

bsema.acquire()

bsema.release()

bsema.release()