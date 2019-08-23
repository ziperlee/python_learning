"""
 Create by zipee on 2019/3/22.
"""
__author__ = 'zipee'

import heapq as h

before_sort = [5,8,7,2,3,1,0,9]
after_sort = []

[h.heappush(after_sort, v) for v in before_sort]
print(after_sort)
[print(h.heappop(after_sort)) for _ in range(len(before_sort))]
