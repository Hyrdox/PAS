import socket


def udp_client_ip_to_hostname():
    server = '127.0.0.1'
    port = 2906

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ip_address = input("Enter IP address: ")
        s.sendto(ip_address.encode(), (server, port))
        response, addr = s.recvfrom(1024)
        print("Hostname:", response.decode())


if __name__ == "__main__":
    udp_client_ip_to_hostname()
