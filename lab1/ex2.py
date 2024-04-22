def skopiuj_grafike(nazwa_wejsciowego_pliku, nazwa_nowego_pliku):
    try:
        with open(nazwa_wejsciowego_pliku, 'rb') as plik_wejsciowy:
            dane = plik_wejsciowy.read()
            with open(nazwa_nowego_pliku, 'wb') as plik_wyjsciowy:
                plik_wyjsciowy.write(dane)
        print("Plik został skopiowany pomyślnie!")
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku.")


nazwa_wejsciowego_pliku = input("Podaj nazwę pliku graficznego do skopiowania: ") + ".png"
nazwa_nowego_pliku = "lab1zad1.png"
skopiuj_grafike(nazwa_wejsciowego_pliku, nazwa_nowego_pliku)