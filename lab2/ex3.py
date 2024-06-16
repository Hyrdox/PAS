import socket


def tcp_client_loop():
    server = '127.0.0.1'
    port = 2900

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))

        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())
            response = s.recv(1024)
            print("Received:", response.decode())


if __name__ == "__main__":
    tcp_client_loop()
