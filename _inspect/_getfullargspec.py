"""
 Create by zipee on 2019/7/14.
"""
__author__ = 'zipee'

# 获取函数参数定义等基础信息

def f(a):
    print('aa')

import inspect
print(inspect.getfullargspec(f))