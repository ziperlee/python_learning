"""
 Create by zipee on 2019/4/6.
"""
__author__ = 'zipee'

import time
from functools import wraps


def running_time(y):
    def decorator(f):
        @wraps(f)
        def wapper(x):
            t1 = time.time()
            f(x+y)
            t2 = time.time()
            print(t2 - t1)
        return wapper
    return decorator

# @running_time(1)
def func(x):
    time.sleep(x)
    print('haha')

new_func = running_time(1)(func)

new_func(1)
# func(1)
print(func.__name__)

#####################

def running_time2(y):
    def decorator(f):
        @wraps(f)
        def wapper(*args, **kwargs):#self,
            t1 = time.time()
            f(*args, **kwargs)#self,
            t2 = time.time()
            print(t2 - t1)
        return wapper
    return decorator



class C:
    @running_time2(1)
    def mysleep(self, x):
        time.sleep(x)

    @staticmethod
    @running_time2(0)
    def mystatic(x):
        time.sleep(x)

    @classmethod
    @running_time2(0)
    def myclassmethod(cls, x):
        time.sleep(x)
c = C()
c.mysleep(1)
C.mystatic(1)
C.myclassmethod(1)
print(C.mystatic.__name__)
