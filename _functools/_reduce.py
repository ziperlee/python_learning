"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

from functools import reduce

sum = reduce(lambda x,y:x+y, range(1,5))
print(sum)