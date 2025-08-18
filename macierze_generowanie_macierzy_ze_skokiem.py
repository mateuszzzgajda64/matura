def policzIleLiczb(poczatek , koniec , skok):
    return (koniec - poczatek) // skok + 1

def policzIloscWierszy(iloscliczb):
    for d in range(2 , iloscliczb + 1):
        if iloscliczb % d == 0:
            return d
    return 1

def policzIloscKolumn(iloscliczb  , iloscwierszy):
    return iloscliczb // iloscwierszy

def generujMacierz(poczatek , skok , iloscwierszy , ilosckolumn):
    macierz = []
    licznik = 0
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(poczatek + skok * licznik)
            licznik = licznik + 1
        macierz.append(wiersz)
    return macierz

poczatek = int(input())
koniec = int(input())
skok = int(input())

iloscliczb = policzIleLiczb(poczatek , koniec, skok)
iloscwierszy = policzIloscWierszy(iloscliczb)
ilosckolumn = policzIloscKolumn(iloscliczb , iloscwierszy)

macierz = (generujMacierz(poczatek , skok , iloscwierszy , ilosckolumn))

for i in macierz:
    print(*i)
