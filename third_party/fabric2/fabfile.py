"""
 Created by liwei on 2020/1/14.
"""
from functools import wraps

from fabric.api import env, roles, run, hide, settings, cd, sudo, execute

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@decorator
def f(a):
    print('this is f')
    print(a)


