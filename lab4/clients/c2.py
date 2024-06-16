import socket

def echo_client():
    host = '127.0.0.1'
    port = 2901

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = b'Hello, echo server'
        client_socket.sendall(message)
        data = client_socket.recv(1024)
        print("Echoed message:", data.decode())

if __name__ == "__main__":
    echo_client()
