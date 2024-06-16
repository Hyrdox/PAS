import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('httpbin.org', 80))

user_data = "name=John&age=30"
content_length = len(user_data)

http_request = f"POST /post HTTP/1.1\r\nHost: httpbin.org\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n{user_data}"
client_socket.sendall(http_request.encode())

response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

client_socket.close()

header, body = response.split(b"\r\n\r\n", 1)
print(body.decode())
