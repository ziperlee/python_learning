"""
 Create by zipee on 2019/4/7.
"""
__author__ = 'zipee'

from itertools import islice

class C:
    def __init__(self):
        self.l = [1,2,3,4,5,6,7,8,9,0]

    def __iter__(self):
        for i in self.l:
            yield i

c = C()
print(list(islice(c, 0, 5)))