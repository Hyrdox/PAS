import socket

def udp_calculator_client():
    host = '127.0.0.1'
    port = 2903

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        expression = "12 + 5"
        client_socket.sendto(expression.encode(), (host, port))
        data, server = client_socket.recvfrom(1024)
        print("Result:", data.decode())

if __name__ == "__main__":
    udp_calculator_client()
