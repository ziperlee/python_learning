"""
 Create by zipee on 2019/3/10.
"""
__author__ = 'zipee'

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    print(msg)
    emit('server_response', {'data': msg['data']})


@socketio.on('connect_event', namespace='/test')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')