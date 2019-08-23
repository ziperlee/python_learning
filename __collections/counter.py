"""
 Create by zipee on 2019/3/22.
"""
__author__ = 'zipee'


from collections import Counter

l = [1,2,3,4,3,2,3,3,7]
c = Counter(l)
print(c)
print(c[3])
print(c.most_common())
print(c.most_common(1))
print(c.get(3))
print(c[5])
c[5] += 1
print(c[5])