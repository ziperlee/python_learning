# from redis import Redis
#
# redis = Redis()
# redis.set('haha', 2)


def f():
    try:
        1 / 0
    except Exception as e:
        raise e


f()
