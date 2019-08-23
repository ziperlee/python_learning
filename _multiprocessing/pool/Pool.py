"""
 Create by zipee on 2019/1/6.
"""
__author__ = 'zipee'

from multiprocessing.pool import Pool


def work(a):
    pass

if __name__ == '__main__':
    pool = Pool(3)
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

