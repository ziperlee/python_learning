"""
 Create by zipee on 2019/1/5.
"""
from time import sleep

__author__ = 'zipee'

from threading import Timer

# Timer 指定时间延迟调用函数，函数运行完则结束
# 若要重复调用则要嵌套调用

def func_timer():
    print("func_timer is called")
    timer = Timer(1, func_timer)
    timer.start()

if __name__ == "__main__":
    timer = Timer(2, func_timer)
    timer.start()

    # sleep(1)
    timer.cancel()