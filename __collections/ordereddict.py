"""
 Create by zipee on 2019/3/22.
"""
__author__ = 'zipee'

from collections import OrderedDict

od = OrderedDict()
od['5'] = 1
od['1'] = 1
od['2'] = 1
print(od)
print('od遍历输出:', {k: v for k, v in od.items()})
od.popitem()
print(od)


d1 = {'b':1, 1:2, 2:3, 'a':1, 'hah':1}
print('d1遍历输出:')

for k, v in d1.items():
    print(k, v)

d2 = {'a':1, 'hah':1, 2:3, 1:2, 'b':1}
print('d2遍历输出:')

for k, v in d2.items():
    print(k, v)

# dict中若k,v 均相等则两个dict相等
print('dict 判等：')
print(d1 == d2)