"""
 Create by zipee on 2019/3/30.
"""
__author__ = 'zipee'

from greenlet import getcurrent as get_ident

print(get_ident())
a = {get_ident(): '1'}
print(a)