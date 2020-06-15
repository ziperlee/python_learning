"""
 Created by liwei on 2020/6/15.
"""
from random import randint


def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist) - 1)
        yield alist.pop(c)


a = ["aa", "bb", "cc"]

c = mygen(a)

print(c)

for i in c:
    print(i)