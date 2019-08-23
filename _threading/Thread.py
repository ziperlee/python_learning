"""
 Create by zipee on 2019/1/5.
"""
__author__ = 'zipee'

from threading import Thread
from time import sleep, ctime
import click

loops = [4, 2]

@click.group()
def main():
    pass

def loop(nloop, nsec):
    print(f"start loop {nloop} at: {ctime()}")
    sleep(nsec)
    print(f"loop {nloop} done at: {ctime()}")

@main.command()
# 创建线程示例，传递函数
def main1():
    threads = []
    for i in range(len(loops)):
        thread = Thread(target=loop, args=(i, loops[i]))
        threads.append(thread)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print(f"all done at: {ctime()}")

@main.command()
# 创建线程示例，传递可调用的类实例
def main2():
    class ThreadFunc:
        def __init__(self, func, args, name=""):
            self.func = func
            self.args = args
            self.name = name

        def __call__(self, *args, **kwargs):
            self.func(*self.args)


    threads = []
    for i in range(len(loops)):
        thread = Thread(target=ThreadFunc(loop, (i, loops[i])))
        threads.append(thread)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print(f"all done at: {ctime()}")

@main.command()
# 子类化的线程类
def main3():
    class MyThread(Thread):
        def __init__(self, func, args, name=""):
            super().__init__()
            # Thread.__init__(self)
            self.func = func
            self.args = args
            self.name = name

        def run(self):
            self.func(*self.args)

    threads = []
    for i in range(len(loops)):
        thread = MyThread(loop, (i, loops[i]))
        threads.append(thread)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print(f"all done at: {ctime()}")





if __name__ == "__main__":
    main()

