import socket

def get_time_from_server():
    server = 'time.nist.gov'
    # Wykorzystałem time.nist.gov, ponieważ on daje odpowiedź.
    # W przypadku próby połączenia z ntp.task.gda.pl dostaję komunikat "Timed out."
    port = 13
    buffer_size = 1024
    retries = 5
    timeout = 5

    for attempt in range(retries):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((server, port))
                data = s.recv(buffer_size)
                print("Current date and time from server:", data.decode())
                return
        except (socket.timeout, ConnectionRefusedError, TimeoutError) as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                print("Retrying...")
            else:
                print("All attempts failed. Please check the server status or your network connection.")

if __name__ == "__main__":
    get_time_from_server()
