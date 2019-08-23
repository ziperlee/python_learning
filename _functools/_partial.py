"""
 Create by zipee on 2019/7/7.
"""
__author__ = 'zipee'

from functools import partial

# 固定函数参数，返回新的函数
def mul(x, y):
    return x * y

double = partial(mul, y=2)

print(double(3))