import socket


def echo_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = input("Wprowadź wiadomość do wysłania: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024)
            print("Odpowiedź serwera:", response.decode())
    finally:
        client_socket.close()


if __name__ == '__main__':
    echo_client('127.0.0.1', 6666)
