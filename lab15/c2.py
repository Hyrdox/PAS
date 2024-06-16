import socket


def weather_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            command = input("Wpisz 'pogoda' aby otrzymać dane pogodowe lub 'exit' aby zakończyć: ")
            if command.lower() == 'exit':
                break
            if command.lower() == 'pogoda':
                client_socket.sendall(command.encode())
                response = client_socket.recv(1024)
                print("Odpowiedź serwera:", response.decode())
            else:
                print("Nieznana komenda")
    finally:
        client_socket.close()


if __name__ == '__main__':
    weather_client('127.0.0.1', 6667)
