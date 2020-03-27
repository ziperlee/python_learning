"""
 Created by liwei on 2019/12/18.
"""
import logging
from multiprocessing.pool import ThreadPool
from threading import current_thread

logger = logging.getLogger(current_thread().getName())
# 默认warning级别
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - thread: %(thread)d- %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logging.basicConfig(level=logging.DEBUG)


def worker():

    i = 0
    while True:
        logger.info("===================================")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info(f"this is thread ")
        logger.info("===================================")
        i += 1
        if i > 10:
            break


if __name__ == "__main__":
    pool = ThreadPool(10)
    for _ in range(100):
        pool.apply_async(worker)

    pool.close()
    pool.join()

    # logger.info('ahahah')
    # logging.info('ahahah')
