import socket

def echo_server():
    host = '127.0.0.1'
    port = 2901

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                data = client_socket.recv(1024)
                if data:
                    client_socket.sendall(data)

if __name__ == "__main__":
    echo_server()
