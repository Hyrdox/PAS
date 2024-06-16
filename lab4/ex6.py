import socket

def udp_hostname_to_ip_server():
    host = '127.0.0.1'
    port = 2905

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                hostname = data.decode()
                try:
                    ip_address = socket.gethostbyname(hostname)
                except socket.gaierror:
                    ip_address = "Unknown host"
                server_socket.sendto(ip_address.encode(), client_address)

if __name__ == "__main__":
    udp_hostname_to_ip_server()
