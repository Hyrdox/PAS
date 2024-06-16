import socket

server_address = ('212.182.24.27', 8080)

def fetch_part(range_header):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    http_request = f"GET /image.jpg HTTP/1.1\r\nHost: 212.182.24.27\r\nRange: {range_header}\r\n\r\n"
    client_socket.sendall(http_request.encode())

    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    client_socket.close()
    return response.split(b"\r\n\r\n", 1)[1]

part1 = fetch_part("bytes=0-99999")
part2 = fetch_part("bytes=100000-199999")
part3 = fetch_part("bytes=200000-")

with open("image.jpg", "wb") as f:
    f.write(part1 + part2 + part3)
