"""
 Created by liwei on 2020/2/16.
"""
import time
from hashlib import md5, sha1

def timeit(f):
    def wapper(*args, **kwargs):
        t1 = time.time()
        f(*args, **kwargs)
        t2 = time.time()
        print(f'cost: {round((t2 - t1), 3)}s')
    return wapper

a = 'asdfnawoeihzoxuv90zv0a9w8erq3ji34l;rej;lgijsdo;iuvzoixcvjoz;ij'*1000000

# 内置hash函数无法进程间运算一致，结果收对象id等因素影响
print(f'hash(a) = {hash(a)}')

@timeit
def md5_test():
    m = md5()
    m.update(a.encode('utf-8'))
    print(f'md5(a) = {m.hexdigest()}')

@timeit
def sha1_test():
    sha = sha1()
    sha.update(a.encode('utf-8'))
    print(f'sha1(a) = {sha.hexdigest()}')

if __name__ == '__main__':
    md5_test()
    sha1_test()
    print(len(a))