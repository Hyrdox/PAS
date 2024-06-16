import socket
import base64
import hashlib


host = 'echo.websocket.org'
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

key = base64.b64encode(hashlib.sha1(b'python-websocket').digest())

handshake = (
    "GET / HTTP/1.1\r\n"
    "Host: {host}\r\n"
    "Upgrade: websocket\r\n"
    "Connection: Upgrade\r\n"
    "Sec-WebSocket-Key: {key}\r\n"
    "Sec-WebSocket-Version: 13\r\n"
    "\r\n"
).format(host=host, key=key.decode())

sock.send(handshake.encode())

response = sock.recv(1024)
print(response.decode())

sock.close()