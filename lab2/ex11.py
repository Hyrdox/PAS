import socket

def tcp_client_20char_message():
    server = '127.0.0.1'
    port = 2908
    message = input("Enter message: ")

    # Ensure the message is exactly 20 characters long
    if len(message) < 20:
        message = message.ljust(20)
    elif len(message) > 20:
        message = message[:20]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        s.sendall(message.encode())
        response = s.recv(20)
        print("Received:", response.decode())

if __name__ == "__main__":
    tcp_client_20char_message()
