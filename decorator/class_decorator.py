"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

import time
from functools import wraps

class runtime:
    def __init__(self, y):
        self.y = y

    # def __get__(self, instance, owner):
    #     def wappers():
    #         beg = time.time()
    #         self.func()
    #         print(f'run time {time.time()-beg}')
    #     return wappers

    def __call__(self, func):
        @wraps(func)
        def wappers(c_self, x):
            beg = time.time()
            res = func(c_self, self.y + x)
            print(f'run time {time.time()-beg}')
            return res
        return wappers


@runtime(1)
def mysleep(x):
    time.sleep(x)

class C:
    @runtime(1)
    def mysleep(self, x):
        time.sleep(x)

# mysleep(1)
# print(mysleep.__name__)

# c = C()
# c.mysleep(1)

#######################
class runtime2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        beg = time.time()
        res = self.func()
        print(f'run time {time.time()-beg}')
        return res

@runtime2
def mysleep2():
    time.sleep(1)

mysleep2()
