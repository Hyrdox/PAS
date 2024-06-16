import socket


def handle_request(request):
    headers = request.split("\r\n")
    method, path, _ = headers[0].split()

    if path == "/":
        with open("index.html", "rb") as f:
            body = f.read()
        response = (
                       "HTTP/1.1 200 OK\r\n"
                       "Content-Type: text/html\r\n"
                       f"Content-Length: {len(body)}\r\n"
                       "\r\n"
                   ).encode() + body
    else:
        with open("404.html", "rb") as f:
            body = f.read()
        response = (
                       "HTTP/1.1 404 Not Found\r\n"
                       "Content-Type: text/html\r\n"
                       f"Content-Length: {len(body)}\r\n"
                       "\r\n"
                   ).encode() + body

    return response


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8001))
server_socket.listen(1)

print("Server is running on http://127.0.0.1:8001/")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    response = handle_request(request)
    client_socket.sendall(response)
    client_socket.close()
