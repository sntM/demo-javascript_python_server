from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('got a connect')
    socketio.emit('response', {'server': 'be my guest'})

@socketio.on('client_message')
def print_reply(text):
    print(text)

if __name__ == '__main__':
    socketio.run(app)
