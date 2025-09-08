n = int(input())

slownik1 = {}

for klucz in range(n):
    klucz = input()
    wartosc = input()
    slownik1[klucz] = wartosc

def czyWiecejNizSrednia(slownik):
    nowy = {}
    suma = 0
    srednia = 0
    for klucz in slownik:
        suma = suma + int(slownik[klucz])

    srednia = suma / len(slownik)

    for klucz in slownik:
        if int(slownik[klucz]) > srednia:
            nowy[klucz] = slownik[klucz]
    return nowy

nowy = czyWiecejNizSrednia(slownik1)

for k , v in nowy.items():
    print(f"{k}: {v}")
