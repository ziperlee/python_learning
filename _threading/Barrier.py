"""
 Create by zipee on 2019/1/5.
"""
from time import sleep

__author__ = 'zipee'

# 栅栏，也叫屏障。可以想象成路障、道闸

# 构造方法：
#
# threading.Barrier(parties, action=None, timeout=None)
#
# 构建Barrier对象，parties 指定参与方数目，timeout是wait方法未指定时超时的默认值。
#
# n_waiting    当前在栅栏中等待的线程数
#
# parties        通过栅栏所需的线程数
#
# wait(timeout=None) 等待通过栅栏，返回0到线程数-1的整数(barrier_id)，每个线程返回不同。如果wait方法设置了超时，并超时发送，栅栏将处于broken状态

# Barrier实例的方法：
#
# broken  检测栅栏是否处于打破的状态，返回True或False
#
# abort()  将栅栏置于broken状态，等待中的线程或者调用等待方法的线程都会抛出threading.BrokenBarrieError异常，直到reset方法来恢复栅栏
#
# reset()  恢复栅栏，重新开始拦截

# 应用场景：
#
# 并发初始化
#
# 所有线程都必须初始化完成后，才能继续工作，例如运行前加载数据，检查，如果这些工作没完成就不能正常工作运行。
#
# 10个线程做10种工作准备，每个线程负责一种工作，只有10个线程都完成后，才能继续工作，先完成的要等待后完成的线程。
#
# 例如，启动一个程序，需要先加载磁盘文件、缓存预热、初始化连接池等工作，这些工作可以齐头并进，不过只有都满足了，程序才能继续向后执行。假设数据库链接失败，则初始化工作失败，就要abort，栅栏broken，所有线程收到异常退出。
#
#
#
# 工作量
#
# 有10个计算任务，完成6个，就算工作完成。

from threading import Barrier, Thread


def work(barrier):
    print(f"n_waiting: {barrier.n_waiting}")
    bid = barrier.wait()  # 阻塞等待栅栏放开  # 参与者的id，返回0到线程数减1的数值
    print(f"after barrier {bid}")

def main1():
    barrier = Barrier(3)
    for i in range(4):
        thread = Thread(target=work, args=(barrier,), name=f'barrier {i}: ')
        thread.start()
        sleep(1)

if __name__ == "__main__":
    main1()