"""
 Create by zipee on 2019/7/14.
"""
from functools import wraps

__author__ = 'zipee'

import inspect

# 获取函数参数定义等基础信息

def f(a=1):
    print('aa')

# print(inspect.getfullargspec(f))

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@decorator
def f(a):
    print('this is f')

if __name__ == '__main__':
    f_args = inspect.getargspec(f)
    print(f'f_args: {f_args}')
    f_args2 = inspect.getfullargspec(f)
    print(f'f_args2: {f_args2}')