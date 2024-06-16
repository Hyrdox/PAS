import socket
import threading
import random


class ClientThread(threading.Thread):
    def __init__(self, connection, address, target_number):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.target_number = target_number

    def run(self):
        print(f"Połączono z {self.address}")
        self.connection.sendall("Zgadnij liczbę od 1 do 100: ".encode())
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            try:
                guess = int(data.decode().strip())
                if guess < self.target_number:
                    self.connection.sendall("Za mało\n".encode())
                elif guess > self.target_number:
                    self.connection.sendall("Za dużo\n".encode())
                else:
                    self.connection.sendall("Gratulacje! Odgadłeś liczbę.\n".encode())
                    break
            except ValueError:
                self.connection.sendall("Błąd: Podaj liczbę\n".encode())
        self.connection.close()
        print(f"Rozłączono z {self.address}")


class GuessingServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def run(self):
        print("Serwer nasłuchuje na porcie:", self.port)
        while True:
            client_conn, client_addr = self.server_socket.accept()
            target_number = random.randint(1, 100)
            client_thread = ClientThread(client_conn, client_addr, target_number)
            client_thread.start()


if __name__ == '__main__':
    server = GuessingServer('127.0.0.1', 6666)
    server.run()
