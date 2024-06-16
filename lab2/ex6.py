import socket


def udp_client_calculator():
    server = '127.0.0.1'
    port = 2902

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            num1 = input("Enter first number: ")
            operator = input("Enter operator (+, -, *, /): ")
            num2 = input("Enter second number: ")

            message = f"{num1} {operator} {num2}"
            s.sendto(message.encode(), (server, port))
            response, addr = s.recvfrom(1024)
            print("Received:", response.decode())


if __name__ == "__main__":
    udp_client_calculator()
