"""
 Created by liwei on 2020/6/15.
"""


def gen():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = f"get: {receive}"
        print(value)


g = gen()

# 通过g.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置
a = g.send(None)
print(f'a = {a}')

# 生成器函数最大的特点是可以接受外部传入的一个变量，并根据变量内容计算结果后返回。这一切都是靠生成器内部的send()函数实现的
# receive = yield value 拆解
# receive = value
# value = f"get: {receive}"
# yield value
b = g.send('hello')
print(f'b = {b}')

c = g.send(123456)
print(f'c = {c}')

g.send('e')
