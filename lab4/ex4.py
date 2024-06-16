import socket

def udp_calculator_server():
    host = '127.0.0.1'
    port = 2903

    def calculate(expression):
        try:
            num1, operator, num2 = expression.split()
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                return str(num1 + num2)
            elif operator == '-':
                return str(num1 - num2)
            elif operator == '*':
                return str(num1 * num2)
            elif operator == '/':
                return str(num1 / num2)
            else:
                return "ERROR: Invalid operator"
        except Exception as e:
            return f"ERROR: {str(e)}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                expression = data.decode()
                result = calculate(expression)
                server_socket.sendto(result.encode(), client_address)

if __name__ == "__main__":
    udp_calculator_server()
