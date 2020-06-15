"""
 Created by liwei on 2020/6/15.
"""


def test1():
    def g1():
        yield range(5)

    def g2():
        yield from range(5)
        # it1 = g1()

    it1 = g1()
    print(it1)

    it2 = g2()
    print(it2)

    # yield就是将range这个可迭代对象直接返回了
    for x in it1:
        print(x)

    # yield from解析了range对象，将其中每一个item返回了
    for x in it2:
        print(x)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


f = fab(5)

print(f)


def test2():
    def f_wrapper(fun_iterable):
        print('start')

        for item in fun_iterable:
            yield item
        print('end')

    wrap = f_wrapper(fab(5))

    for i in wrap:
        print(i)


# yield from后面必须跟iterable对象(可以是生成器，迭代器)
# 相较于test2：yield from iterable本质上等于for item in iterable: yield item的缩写版
def test3():
    def f_wrapper2(fun_iterable):
        print('start')

        yield from fun_iterable  # 注意此处必须是一个可迭代对象
        print('end')

    wrap = f_wrapper2(fab(5))

    for i in wrap:
        print(i)


if __name__ == '__main__':
    # test1()
    test2()
