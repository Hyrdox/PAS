import socket

def echo_client_with_confirmation():
    host = '127.0.0.1'
    port = 2907
    message = b'Hello, confirmation echo server'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message[:20])
        data = client_socket.recv(20)
        print("Echoed message:", data.decode())

if __name__ == "__main__":
    echo_client_with_confirmation()
