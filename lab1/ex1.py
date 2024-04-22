def skopiuj_do_nowego_pliku(nazwa_wejsciowego_pliku, nazwa_nowego_pliku):
    try:
        with open(nazwa_wejsciowego_pliku, 'r') as plik_wejsciowy:
            dane = plik_wejsciowy.read()
            with open(nazwa_nowego_pliku, 'w') as plik_wyjsciowy:
                plik_wyjsciowy.write(dane)
        print("Plik został skopiowany pomyślnie!")
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku.")


nazwa_wejsciowego_pliku = input("Podaj nazwę pliku tekstowego do skopiowania: ") + ".txt"
nazwa_nowego_pliku = "lab1zad1.txt"
skopiuj_do_nowego_pliku(nazwa_wejsciowego_pliku, nazwa_nowego_pliku)