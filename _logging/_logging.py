"""
 Created by liwei on 2019/12/17.
"""
import os
import logging
from logging.handlers import RotatingFileHandler


def singleton(cls):
  instances = {}
  def _singleton(*args,**kwargs):
    if cls not in instances:
      instances[cls] = cls(*args,**kwargs)
    return instances[cls]
  return _singleton


@singleton
class Logger1(object):
    _instance = None
    default_log_file = "log/service.log"
    default_log_level = logging.INFO
    default_log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(
        self,
        log_file="log/service.log",
        log_level=logging.INFO,
        log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ):
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        formatter = logging.Formatter(log_format)

        rt = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=10)
        rt.setLevel(log_level)
        rt.setFormatter(formatter)

        self.logger = logging.getLogger("log")
        self.logger.setLevel(log_level)
        self.logger.addHandler(rt)


class Logger2(object):
    _instance = None
    default_log_file = "log/service.log"
    default_log_level = logging.INFO
    default_log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __new__(cls, *args,
                log_file="log/service.log",
                log_level=logging.INFO,
                log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger2, cls).__new__(cls, *args, **kwargs)
            log_dir = os.path.dirname(log_file)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            formatter = logging.Formatter(log_format)

            rt = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=10)
            rt.setLevel(log_level)
            rt.setFormatter(formatter)

            cls._instance.logger = logging.getLogger("log")
            cls._instance.logger.setLevel(log_level)
            cls._instance.logger.addHandler(rt)

        return cls._instance


if __name__ == '__main__':
    logger1 = Logger().get_logger()

    logger2= Logger().get_logger()

    logger1.info('haha')
    logger2.info('asdfas;ldfjal')
    print(logger1 is logger2)