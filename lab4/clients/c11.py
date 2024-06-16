import socket

def udp_syntax_check_client_task_15():
    host = '127.0.0.1'
    port = 2910
    message = "zad15odp;param;foo;value;bar"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Server response:", data.decode())

if __name__ == "__main__":
    udp_syntax_check_client_task_15()
