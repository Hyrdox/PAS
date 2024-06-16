import socket

def udp_hostname_to_ip_client():
    host = '127.0.0.1'
    port = 2905

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        hostname = "www.google.com"
        client_socket.sendto(hostname.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("IP address:", data.decode())

if __name__ == "__main__":
    udp_hostname_to_ip_client()
