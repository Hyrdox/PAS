import socket

def udp_syntax_check_client_task_14():
    host = '127.0.0.1'
    port = 2909
    message = "zad14odp;req;12345;res;67890"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Server response:", data.decode())

if __name__ == "__main__":
    udp_syntax_check_client_task_14()
