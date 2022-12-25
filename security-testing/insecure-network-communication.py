import socket

def send_data(data):
    s = socket.socket()
    s.connect(("example.com", 80))
    s.send(data.encode())

data = "sensitive information"
send_data(data)
