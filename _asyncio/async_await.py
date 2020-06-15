"""
 Created by liwei on 2020/6/15.
"""
import asyncio
from random import randint
from time import sleep
import time


def test1():
    async def mygen(alist):
        while len(alist) > 0:
            c = randint(0, len(alist) - 1)
            print(alist.pop(c))

    a = ["aa", "bb", "cc"]

    c = mygen(a)

    print(c)


def test2():
    # async_generator, 去掉async则为 generator
    # async对生成器是无效的。async无法将一个生成器转换成协程
    async def mygen(alist):
        while len(alist) > 0:
            c = randint(0, len(alist) - 1)
            yield alist.pop(c)

    a = ["aa", "bb", "cc"]

    c = mygen(a)

    print(c)


def test3():
    async def mygen(alist):
        while len(alist) > 0:
            c = randint(0, len(alist) - 1)
            print(alist.pop(c))
            await asyncio.sleep(1)

    strlist = ["ss", "dd", "gg"]

    intlist = [1, 2, 5, 6]

    c1 = mygen(strlist)

    c2 = mygen(intlist)

    loop = asyncio.get_event_loop()

    tasks = [c1, c2]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def test4():
    async def test11():
        print(f"start11:{time.strftime('%X')}")
        await asyncio.sleep(1)
        print(f"end11:{time.strftime('%X')}")

    async def test22():
        print(f"start22:{time.strftime('%X')}")
        # 将导致test11协程不能按时返回
        # sleep(3)
        await asyncio.sleep(3)
        print(f"end22:{time.strftime('%X')}")

    # asyncio.run(test())
    loop = asyncio.get_event_loop()

    tasks = [test11(), test22()]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def test5():
    async def factorial(name, number):
        f = 1
        for i in range(2, number + 1):
            print(f"Task {name}: Compute factorial({i})...")
            await asyncio.sleep(1)
            f *= i
        print(f"Task {name}: factorial({number}) = {f}")

    async def mygen(alist):
        while len(alist) > 0:
            c = randint(0, len(alist) - 1)
            print(alist.pop(c))
            await asyncio.sleep(1)

    strlist = ["ss", "dd", "gg"]
    intlist = [1, 2, 5, 6]

    async def main():
        # Schedule three calls *concurrently*:
        await asyncio.gather(
            # factorial("A", 2),
            # factorial("B", 3),
            # factorial("C", 4),
            mygen(strlist),
            mygen(intlist)
        )

    asyncio.run(main())


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()