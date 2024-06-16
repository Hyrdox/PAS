import socket

def udp_echo_server():
    host = '127.0.0.1'
    port = 2902

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                server_socket.sendto(data, client_address)

if __name__ == "__main__":
    udp_echo_server()
