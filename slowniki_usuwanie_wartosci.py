n = int(input()) #warto zauwazyc ze zamiast usuwac tak naprawde pomijamy dodawanie do nowego slownika niechcianych wartosci

slownik1 = {}

for klucz in range(n):
    klucz = input()
    wartosc = input()
    slownik1[klucz] = wartosc

def czyDel(slownik):
    nowy = {}
    for klucz in slownik:
        if slownik[klucz] != 'Delete':
            nowy[klucz] = slownik[klucz]
    return nowy

nowy = czyDel(slownik1)

for k , v in nowy.items():
    print(f"{k}: {v}")
