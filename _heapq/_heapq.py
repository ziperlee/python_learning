"""
 Create by zipee on 2019/6/9.
"""
__author__ = 'zipee'

import heapq as h

# 创建小顶堆 heapqush heapify
# 弹出最小的元素 heappop
# 弹出最小的元素并压入新元素 heapreplace
# 获取top K大|小的元素 nlargest nsmallest
# 压入新元素并弹出最小元素 heappushpop
# 合并多个已排序数组

before_sort = [5,8,7,2,3,1,0,9]
after_sort = []
sorted1 = [1,3,5,7,9]
sorted2 = [0,2,4,6,8]

print(h.nlargest(2, before_sort))
print(h.nsmallest(2, before_sort))
data = list(h.merge(sorted1, sorted2))
print(data)

# 默认为最小堆|小顶堆
[h.heappush(after_sort, v) for v in before_sort]
print(after_sort)
[print(h.heappop(after_sort)) for _ in range(len(before_sort))]

print(before_sort)
# 使用heapify进行原地堆化
h.heapify(before_sort)
print(before_sort)
[print(h.heappop(before_sort)) for _ in range(len(before_sort))]
