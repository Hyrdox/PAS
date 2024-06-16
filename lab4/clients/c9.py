import socket

def udp_syntax_check_client_task_13():
    host = '127.0.0.1'
    port = 2908
    message = "zad13odp;src;2900;dst;35211;data;hello :)"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Server response:", data.decode())

if __name__ == "__main__":
    udp_syntax_check_client_task_13()
