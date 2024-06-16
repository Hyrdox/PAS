import socket

def echo_server_max_length():
    host = '127.0.0.1'
    port = 2906
    max_length = 20

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                data = client_socket.recv(max_length)
                if data:
                    client_socket.sendall(data[:max_length])

if __name__ == "__main__":
    echo_server_max_length()
