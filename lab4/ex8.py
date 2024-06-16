import socket

def echo_server_with_confirmation():
    host = '127.0.0.1'
    port = 2907
    max_length = 20

    def receive_all(sock, length):
        data = b''
        while len(data) < length:
            packet = sock.recv(length - len(data))
            if not packet:
                break
            data += packet
        return data

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                data = receive_all(client_socket, max_length)
                if len(data) == max_length:
                    client_socket.sendall(data)

if __name__ == "__main__":
    echo_server_with_confirmation()
