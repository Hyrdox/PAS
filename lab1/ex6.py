import socket
import sys


def sprawdz_polaczenie(adres, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((adres, port))
        sock.close()
        return True
    except socket.error:
        return False


if len(sys.argv) != 3:
    print("Użycie: python nazwa_programu.py <adres_serwera> <numer_portu>")
    sys.exit(1)

adres_serwera = sys.argv[1]
numer_portu = int(sys.argv[2])

if sprawdz_polaczenie(adres_serwera, numer_portu):
    print("Udało się nawiązać połączenie z", adres_serwera, "na porcie", numer_portu)
else:
    print("Nie udało się nawiązać połączenia z", adres_serwera, "na porcie", numer_portu)