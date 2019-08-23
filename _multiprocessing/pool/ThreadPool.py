"""
 Create by zipee on 2019/1/6.
"""
from threading import current_thread


__author__ = 'zipee'

from multiprocessing.pool import ThreadPool

def work(a):
    thread_name = current_thread().name
    print(f"this is thread: {thread_name}")
    return f"thread: {thread_name} return {a}"

if __name__ == '__main__':
    pool = ThreadPool(3)
    for i in range(10):
        result = pool.apply(work, (i,))
        print(result)
    print("apply all done")

###########################################
    results = []
    for i in range(10):
        result = pool.apply_async(work, (i,))
        results.append(result)
    for result in results:
        print(result.get())
    print("apply all done")
###########################################
    results = pool.map(work, (i,))
    print(results)
###########################################
    results = pool.map_async(work, (i,))
    print(results.get())

    pool.close()
    pool.join()

