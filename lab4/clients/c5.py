import socket

def udp_ip_to_hostname_client():
    host = '127.0.0.1'
    port = 2904

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        ip_address = "8.8.8.8"
        client_socket.sendto(ip_address.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Hostname:", data.decode())

if __name__ == "__main__":
    udp_ip_to_hostname_client()
