"""
 Create by zipee on 2019/1/5.
"""
from time import sleep

__author__ = 'zipee'

from threading import Event, Thread

# 事件设置后所有的监听线程都会被唤醒
class MyThread(Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        print(f"thread:{self.name} is waiting..")
        self.signal.wait()
        print(f"thread:{self.name} await")

def main():
    signal = Event()
    for i in range(3):
        MyThread(signal).start()

    sleep(1)
    signal.set()

if __name__ == "__main__":
    main()