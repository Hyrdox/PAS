import socket

def check_msg_syntax_task_15(msg):
    try:
        parts = msg.split(';')
        if len(parts) != 5:
            return "BAD SYNTAX"
        if parts[0] == 'zad15odp' and parts[1] == 'param' and parts[3] == 'value':
            return "TAK"
        else:
            return "NIE"
    except Exception:
        return "BAD SYNTAX"

def udp_syntax_check_server_task_15():
    host = '127.0.0.1'
    port = 2910

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                message = data.decode()
                response = check_msg_syntax_task_15(message)
                server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_syntax_check_server_task_15()
