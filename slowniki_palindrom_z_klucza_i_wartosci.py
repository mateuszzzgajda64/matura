n = int(input())
slownik1 = {}

for i in range(n):
    klucz = input()
    wartosc = input()
    slownik1[klucz] =  wartosc

def palindromyWSlowniku(slownik):
    dict = {}
    for klucz in slownik:
        slowo = klucz + slownik[klucz]
        if slowo == slowo[::-1]:
            dict[klucz] = slownik[klucz]
    return dict


nowy = palindromyWSlowniku(slownik1)

for k , v in nowy.items():
    print(f"{k}: {v}")
