import socket
import sys


def pobierz_adres_ip(hostname):
    try:
        adres_ip = socket.gethostbyname(hostname)
        return adres_ip
    except socket.gaierror as e:
        print("Nie można znaleźć adresu IP dla podanej nazwy hosta:", e)
        return None


if len(sys.argv) != 2:
    print("Użycie: python nazwa_programu.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]
adres_ip = pobierz_adres_ip(hostname)

if adres_ip:
    print("Adres IP dla hosta", hostname, "to:", adres_ip)
