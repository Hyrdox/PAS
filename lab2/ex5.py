import socket

def udp_client_loop():
    server = '127.0.0.1'
    port = 2901

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            s.sendto(message.encode(), (server, port))
            response, addr = s.recvfrom(1024)
            print("Received:", response.decode())

if __name__ == "__main__":
    udp_client_loop()
