"""
 Create by zipee on 2019/5/11.
"""
__author__ = 'zipee'

# start 指定index的起始位置，支持关键字传参
# 没有stop，step
# 即使逆序遍历，index仍是正序

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasons_d = {'Spring': 'Spring', 'Summer': 'Summer', 'Fall': 'Fall', 'Winter': 'Winter'}

print(enumerate(seasons))
print(type(enumerate(seasons)))
print(list(enumerate(seasons)))
print(list(enumerate(seasons_d)))
print(seasons_d.items())
print(list(seasons_d.items()))

print(list(enumerate(seasons, 1)))
print(list(enumerate(seasons, start=1)))

a = [4,1,2,3]
print([i for i in enumerate(a[::-1])])