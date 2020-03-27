"""
 Created by liwei on 2019/12/18.
"""

import logging
import sys
import uuid

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | %(uuid)s | %(interface)s | %(message)s | %(cost)s | %(status)s", "%Y-%m-%d %H:%M:%S")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

if __name__ == '__main__':
    extra = {
        'uuid': uuid.uuid1(),
        'interface': 'upload_binary',
        'cost': 1.2,
        'status': 200
    }
    logger.info('hello world', extra=extra)


