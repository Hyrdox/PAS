import socket

def tcp_client_ensure_full_message():
    server = '127.0.0.1'
    port = 2908
    message = input("Enter message: ")

    if len(message) < 20:
        message = message.ljust(20)
    elif len(message) > 20:
        message = message[:20]

    def send_full(conn, msg):
        total_sent = 0
        while total_sent < len(msg):
            sent = conn.send(msg[total_sent:].encode())
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            total_sent += sent

    def recv_full(conn, length):
        chunks = []
        bytes_recd = 0
        while bytes_recd < length:
            chunk = conn.recv(min(length - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("Socket connection broken")
            chunks.append(chunk)
            bytes_recd += len(chunk)
        return b''.join(chunks)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        send_full(s, message)
        response = recv_full(s, 20)
        print("Received:", response.decode())

if __name__ == "__main__":
    tcp_client_ensure_full_message()
