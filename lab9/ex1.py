import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('httpbin.org', 80)
client_socket.connect(server_address)

http_request = "GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n\r\n"

client_socket.sendall(http_request.encode())

response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

client_socket.close()

header, body = response.split(b"\r\n\r\n", 1)

with open("response.html", "wb") as f:
    f.write(body)
