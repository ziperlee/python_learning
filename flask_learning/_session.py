"""
 Create by zipee on 2019/3/17.
"""
from contextlib import contextmanager

__author__ = 'zipee'

from flask import Flask
from flask_login import LoginManager, login_required, UserMixin, current_user, login_user
from flask_sqlalchemy import SQLAlchemy as _SQLAchemy

class SQLAlchemy(_SQLAchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:ziper520@192.168.190.1:32769/liwei',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # 'DEBUG': True,
    'SECRET_KEY': '\xf4\xaf\xb6W\xe1\x9f\x88X!b\xa0m\xffw\xe50Pv\x18T\xe4\x0f$\x1e',
})

login_manager = LoginManager(app=app)
db = SQLAlchemy(app=app)


class User2(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    # password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def get_user(id):
    user = User2.query.filter_by(id=int(id)).first()
    if user is None:
        raise Exception('user is None')

    return user

@app.route('/')
def index():
    return 'this is index'

@app.route('/login/<int:id>')
def login(id):
    user = User2.query.get(id)
    login_user(user)
    return 'success'

@app.route('/user-detail')
@login_required
def detail():
    user = User2.query.get(current_user.id)
    return f'user name is {user.name}'

@app.route('/register/<int:id>')
def register(id):
    with db.auto_commit():
        user = User2()
        user.id = id
        user.name = f'user:{id}'
        db.session.add(user)
    return 'success'

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)