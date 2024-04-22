import socket


def sprawdz_adres_ip(adres_ip):
    try:
        socket.inet_aton(adres_ip)
        return True
    except socket.error:
        return False


adres_ip = input("Podaj adres IP do sprawdzenia: ")
if sprawdz_adres_ip(adres_ip):
    print("Podany adres IP jest poprawny.")
else:
    print("Podany adres IP jest niepoprawny.")