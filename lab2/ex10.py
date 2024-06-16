import socket


def udp_client_hostname_to_ip():
    server = '127.0.0.1'
    port = 2907

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        hostname = input("Enter hostname: ")
        s.sendto(hostname.encode(), (server, port))
        response, addr = s.recvfrom(1024)
        print("IP Address:", response.decode())


if __name__ == "__main__":
    udp_client_hostname_to_ip()
