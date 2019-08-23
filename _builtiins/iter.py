"""
 Create by zipee on 2019/3/30.
"""
__author__ = 'zipee'

a = {'11':1,'22':2}
b = iter(a)
print(type(b))
for i in b:
    print(i)