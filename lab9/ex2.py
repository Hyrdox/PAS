import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('httpbin.org', 80))

http_request = "GET /image/png HTTP/1.1\r\nHost: httpbin.org\r\n\r\n"
client_socket.sendall(http_request.encode())

response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

client_socket.close()

header, body = response.split(b"\r\n\r\n", 1)

with open("image.png", "wb") as f:
    f.write(body)
