"""
 Create by zipee on 2019/1/5.
"""
from time import sleep

__author__ = 'zipee'

# Condition 可以指定锁，默认使用RLock
# 所以Condition的require()_，release() 完全可以替代Lock，RLock的功能

from threading import Condition, Thread

condition = Condition()
queue = []
MAX = 10

class Consumer(Thread):
    def consume(self):
        global queue
        global condition
        with condition:
            if len(queue) == 0:
                condition.wait()
            queue.pop()
            print(f"consumed 1 item")
            print(f"current queue size is: {len(queue)}")
            condition.notify()

    def run(self):
        for i in range(20):
            self.consume()

class Producer(Thread):
    def produce(self):
        global queue
        global condition
        with condition:
            if len(queue) == MAX:
                condition.wait()
            queue.append(1)
            print(f"producted 1 item")
            print(f"current queue size is: {len(queue)}")
            condition.notify()

    def run(self):
        for i in range(20):
            # sleep(1)  生产者如果不睡眠则容易再次获取到自己释放的锁
            self.produce()

if __name__ == "__main__":
    consumer = Consumer()
    producer = Producer()

    consumer.start()
    producer.start()
