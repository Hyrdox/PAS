import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        print(f"Połączono z {self.address}")
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.sendall(data)
        self.connection.close()
        print(f"Rozłączono z {self.address}")


class EchoServer:
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
            client_thread = ClientThread(client_conn, client_addr)
            client_thread.start()


if __name__ == '__main__':
    server = EchoServer('127.0.0.1', 6666)
    server.run()
