"""
 Create by zipee on 2019/4/26.
"""
__author__ = 'zipee'

from celery import Celery

app = Celery('simple', broker='redis://redis:6379/0')


@app.task()
def add(x, y):
    return x + y

# add.delay(1,2)
# celery -A simple worker -l info
#   -l 必须不然无法看到tasks信息