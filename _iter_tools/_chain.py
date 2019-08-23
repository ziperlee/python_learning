"""
 Create by zipee on 2019/3/30.
"""
__author__ = 'zipee'

from itertools import chain

a = [1,2,3]
b = [4,5,6]

c = chain(a, b)
print(type(c))
for v in c:
    print(v)