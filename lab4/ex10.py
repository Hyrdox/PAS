import socket

def check_msg_syntax_task_14(msg):
    try:
        parts = msg.split(';')
        if len(parts) != 5:
            return "BAD SYNTAX"
        if parts[0] == 'zad14odp' and parts[1] == 'req' and parts[3] == 'res':
            return "TAK"
        else:
            return "NIE"
    except Exception:
        return "BAD SYNTAX"

def udp_syntax_check_server_task_14():
    host = '127.0.0.1'
    port = 2909

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                message = data.decode()
                response = check_msg_syntax_task_14(message)
                server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_syntax_check_server_task_14()
