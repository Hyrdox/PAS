import socket

def date_time_client():
    host = '127.0.0.1'
    port = 2900

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(b'Hello, server')
        data = client_socket.recv(1024)
        print("Current date and time:", data.decode())

if __name__ == "__main__":
    date_time_client()
