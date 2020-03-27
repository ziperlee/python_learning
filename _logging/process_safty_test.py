"""
 Created by liwei on 2019/12/18.
"""
import logging
from multiprocessing.pool import Pool

logger = logging.getLogger("log")
# 默认warning级别
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - process: %(process)d- %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)



def worker():
    i = 0
    while True:
        logger.info("===================================")
        logger.info(f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread "
                    f"this is thread ")
        i += 1
        if i > 10:
            break


if __name__ == "__main__":
    pool = Pool(10)
    for _ in range(100):
        pool.apply_async(worker)

    pool.close()
    pool.join()

    # logger.info('ahahah')
    # logging.info('ahahah')
