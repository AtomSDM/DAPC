import socketio

TOKEN = "" #You donation alert token

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)


@sio.on('donation')
def on_message(data):
    print(data)

sio.connect('wss://socket.donationalerts.ru:443')
sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})
