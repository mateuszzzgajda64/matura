n = int(input())

slownik1 = {}

for i in range(1 , n + 1):
    klucz = i
    slownik1[klucz] = None

def czyPierwsza(slownik):
    for klucz in slownik:
        if klucz < 2:
            slownik[klucz] = False
        else:
            pierwsza = True
            for i in range(2 , int(klucz**0.5) + 1):
                if klucz % i == 0:
                    pierwsza = False
                    break
            slownik[klucz] = pierwsza
    return slownik

nowy = czyPierwsza(slownik1)

for k , v in nowy.items():
    print(f"{k}: {v}")
