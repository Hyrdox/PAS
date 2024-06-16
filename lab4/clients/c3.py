import socket

def udp_echo_client():
    host = '127.0.0.1'
    port = 2902

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = b'Hello, UDP echo server'
        client_socket.sendto(message, (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Echoed message:", data.decode())

if __name__ == "__main__":
    udp_echo_client()
