"""
 Created by liwei on 2020/3/26.
"""
from functools import wraps

import time

from retrying import retry


@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")


@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")


@retry(stop_max_delay=10000)
def stop_after_10_s():
    print("Stopping after 10 seconds")


@retry(wait_fixed=2000)
def wait_2_s():
    print("Wait 2 second between retries")


def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    # return result is None
    # return True
    raise RuntimeError("haah")
    return True

@retry(retry_on_result=retry_if_result_none)
def might_return_none():
    print("Retry forever ignoring Exceptions with no wait if return value is None")


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)

@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    # raise IOError

@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    print(
        "Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError"
    )
    raise RuntimeError


# def test_retry(p):
#     return True


def timeit(start_msg="", end_msg=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            if start_msg:
                print(f"{start_msg}")

            start = time.time()
            data = func(*args, **kwds)

            if end_msg:
                print(f"{end_msg} {calculate_cost_time(start)}")
            else:
                print(f"{func.__name__} {calculate_cost_time(start)}")
            return data

        return wrapper

    return decorator


def calculate_cost_time(start_time):
    """
    计算耗时
    :return:
    """
    end_time = time.time()
    cost_time = end_time - start_time
    if cost_time < 60:
        return "耗时:{}秒".format(round(cost_time, 3))
    elif cost_time < 3600:
        minute_num = cost_time // 60
        second_num = cost_time % 60
        return "耗时:{}分 {}秒".format(minute_num, round(second_num, 3))
    else:
        hour_num = cost_time // (60 * 60)
        minute_left_time = cost_time - hour_num * 60 * 60
        minute_num = minute_left_time // 60
        second_left_time = cost_time - minute_left_time - minute_num * 60
        return "耗时:{}时 {}分 {}秒".format(hour_num, minute_num, round(second_left_time, 3))


count = 1


class TestC:
    def test(self):
        def test_retry(p):
            return True

        @retry(retry_on_result=test_retry)
        def be_tested():
            print('testing')

        be_tested()

    def test_retry(p):
        global count
        if count > 3:
            return False

        count += 1
        print(p)
        return True

    @timeit(start_msg='starting')
    @retry(retry_on_result=test_retry, wait_fixed=2000)
    def test2(self):
        print('testing')
        return 'hello'


if __name__ == "__main__":

    # never_give_up_never_surrender()
    # stop_after_7_attempts()
    # stop_after_10_s()
    # wait_2_s()
    # might_return_none()
    # might_io_error()
    # only_raise_retry_error_when_not_io_error()

    t = TestC()
    t.test2()