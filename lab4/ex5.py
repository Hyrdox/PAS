import socket

def udp_ip_to_hostname_server():
    host = '127.0.0.1'
    port = 2904

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                ip_address = data.decode()
                try:
                    hostname = socket.gethostbyaddr(ip_address)[0]
                except socket.herror:
                    hostname = "Unknown host"
                server_socket.sendto(hostname.encode(), client_address)

if __name__ == "__main__":
    udp_ip_to_hostname_server()
