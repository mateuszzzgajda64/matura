n = int(input())

slownik1 = {}
slownik2 = {}

for i in range(n):
    klucz = input()
    wartosc = input()
    slownik1[klucz] = wartosc

m = int(input())

for i in range(m):
    klucz = input()
    wartosc = input()
    slownik2[klucz] = wartosc

def polacz(slownik1 , slownik2):
    slownik = {}
    for k , v in slownik1.items():
        slownik[k] = v
    for k , v in slownik2.items():
        if k not in slownik:
            slownik[k] = v
    return slownik

nowy = polacz(slownik1 , slownik2)

for k , v in nowy.items():
    print(f"{k}: {v}")
