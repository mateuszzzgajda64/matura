n = int(input())

slownik = {}

def napraw_slownik(slownik):
    nowy = {}

    for k in slownik:
        nowy[k.replace(' ' , '')] = slownik[k]

    nowy2 = {}
    for k , v in nowy.items():
        if v != 0:
            nowy2[k] = v


    x = len(nowy2)
    suma = 0
    for k , v in nowy2.items():
        suma += v
    s = suma / x

    nowy3 = {}
    for k , v in nowy2.items():
        if v >= s:
            nowy3[k] = v
    return nowy3


for i in range(n):
    klucz = input()
    wartosc = int(input())
    slownik[klucz] = wartosc

slownik2 = napraw_slownik(slownik)
slownik3 ={}

for k , v in slownik2.items():
    slownik3[v] = k

for k , v in slownik3.items():
    print(k , '->' , v)

