import socket
import sys


def skanuj_porty(adres, startowy_port, koncowy_port):
    print("Skanowanie portów na serwerze", adres)
    for port in range(startowy_port, koncowy_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            result = sock.connect_ex((adres, port))
            if result == 0:
                print("Port {} jest otwarty".format(port))
            sock.close()
        except KeyboardInterrupt:
            print("\nSkanowanie przerwane.")
            sys.exit()
        except socket.error:
            print("Wystąpił błąd podczas skanowania portu", port)


if len(sys.argv) != 2:
    print("Użycie: python nazwa_programu.py <adres_serwera>")
    sys.exit(1)

adres_serwera = sys.argv[1]
startowy_port = 1
koncowy_port = 1024  # Możemu ustawić na wyższy numer portu, jeśli chcemy skanować więcej portów

skanuj_porty(adres_serwera, startowy_port, koncowy_port)