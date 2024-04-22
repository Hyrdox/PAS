import socket
import sys


def pobierz_hostname(adres_ip):
    try:
        hostname = socket.gethostbyaddr(adres_ip)
        return hostname[0]
    except socket.herror as e:
        print("Nie można znaleźć nazwy hosta dla podanego adresu IP:", e)
        return None


if len(sys.argv) != 2:
    print("Użycie: python nazwa_programu.py <adres_ip>")
    sys.exit(1)

adres_ip = sys.argv[1]
hostname = pobierz_hostname(adres_ip)

if hostname:
    print("Nazwa hosta dla adresu IP", adres_ip, "to:", hostname)