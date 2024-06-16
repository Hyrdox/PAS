import socket

def tcp_client_single_message():
    server = '127.0.0.1'
    port = 2900
    message = "Hello, Server!"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        s.sendall(message.encode())
        response = s.recv(1024)
        print("Received:", response.decode())

if __name__ == "__main__":
    tcp_client_single_message()
