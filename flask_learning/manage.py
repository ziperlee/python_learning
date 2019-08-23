"""
 Create by zipee on 2019/3/30.
"""
__author__ = 'zipee'

from flask import Flask, Blueprint
from flask_caching import Cache

app = Flask(__name__)
app.config.update(
    {
        "CACHE_TYPE": "redis", "CACHE_REDIS_URL": "redis:@//:localhost:6379/0",
        # "DEBUG": True
    }
)
# config = {"CACHE_TYPE": "redis", "CACHE_REDIS_URL": "redis:@//:localhost:6379/0"}
cache = Cache()
cache.init_app(app=app)

bp = Blueprint('user', __name__)
@bp.route('/')
def user_index():
    return 'this is user index'
app.register_blueprint(bp)

@app.route('/')
def index():
    return 'this is index'

@app.route('/cache_test/<int:id>', methods=['POST'])
@cache.cached()
def cache_test(id):
    from flask import request
    got_data = request.get_json()
    import time

    return f"{got_data}.{id}.{time.time()}"

@cache.memoize()
def f_cache(a):
    return a
@app.route('/cache_test2/<int:id>', methods=['POST'])
def cache_test2(id):
    return f"{f_cache(id)}"

if __name__ == '__main__':
    print(cache_test.cache_timeout)
    app.run(host='0.0.0.0', port=6000)
