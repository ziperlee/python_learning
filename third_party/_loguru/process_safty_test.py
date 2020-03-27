"""
 Created by liwei on 2019/12/18.
"""
import sys
from multiprocessing.pool import Pool

from loguru import logger

logger.add("somefile.log", colorize=False, enqueue=True)
def worker():
    i = 0
    while True:
        logger.info("===================================")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info(f"this is thread 12312312312312334534645645756756756")
        logger.info("===================================")
        i += 1
        if i > 5:
            break


if __name__ == "__main__":
    pool = Pool(10)
    for _ in range(100):
        pool.apply_async(worker)

    pool.close()
    pool.join()
