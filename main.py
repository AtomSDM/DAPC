import socketio

TOKEN = "  " #You donation alert token

sio = socketio.Client()

@sio.on('donation')
def on_message(data):
    print(data)

sio.connect('wss://socket.donationalerts.ru:443')
sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})
