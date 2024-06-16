import socket


def guessing_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            response = client_socket.recv(1024)
            print(response.decode(), end="")
            if "Gratulacje" in response.decode():
                break
            guess = input("Podaj liczbę: ")
            client_socket.sendall(guess.encode())
    finally:
        client_socket.close()


if __name__ == '__main__':
    guessing_client('127.0.0.1', 6666)
