plik = open('plansza.txt', 'r')
zapis = open('wyniki4.txt', 'w')

plansza = []

for line in plik:
    plansza.append(list(line.strip().split(' ')))

macierz2 = []

macierz2.append(['0']*102)

for i in range(len(plansza)):
    wiersz = ['0'] + plansza[i] + ['0']
    macierz2.append(wiersz)

macierz2.append(['0']*102)

plansza = macierz2

def czy_jednomasztowiec(plansza , i , j):
    pole = plansza[i][j]
    lgr = plansza[i - 1][j - 1]
    g = plansza[i - 1][j]
    pgr = plansza[i - 1][j + 1]
    l = plansza[i][j - 1]
    p = plansza[i][j + 1]
    ldr = plansza[i + 1][j - 1]
    d = plansza[i + 1][j]
    pdr = plansza[i + 1][j + 1]
    if pole == '1' and lgr == '0' and g == '0' and pgr == '0' and l == '0' and p == '0' and ldr == '0' and d == '0' and pdr == '0':
        return True
    return False
def czy_dwumasztowiec(plansza , i , j):
    pole = plansza[i][j]
    lgr = plansza[i - 1][j - 1]
    g = plansza[i - 1][j]
    pgr = plansza[i - 1][j + 1]
    l = plansza[i][j - 1]
    p = plansza[i][j + 1]
    ldr = plansza[i + 1][j - 1]
    d = plansza[i + 1][j]
    pdr = plansza[i + 1][j + 1]
    if pole == '1':
        if lgr == '1' or g == '1' or pgr == '1' or l == '1' or pdr == '1' or d == '1' or ldr == '1' or p =='1':
            return True
    return False

def f(plansza):
    licznik = 0
    for i in range(1 , len(plansza) - 1):
        for j in range(1 , len(plansza) -1):
            if i !=j:
                if plansza[i][j] == '1' and plansza[j][i] == '1' :
                    if czy_jednomasztowiec(plansza, i, j) and czy_jednomasztowiec(plansza, j , i):
                        licznik += 1


    return licznik // 2

def po_przekatnej(plansza):
    odwiedzone= set()
    jednomasztowiec = 0
    dwumasztowiec = 0

    n = len(plansza) - 2
    for i in range(1 , n + 1):
        if czy_jednomasztowiec(plansza , i , i):
            jednomasztowiec += 1
        if czy_dwumasztowiec(plansza , i , i) and (i , i) not in odwiedzone:
            dwumasztowiec += 1
            for x in range(i-1 , i+2):
                for y in range(i-1 , i+2):
                    odwiedzone.add((x,y))


    for i in range(1 , n + 1):
        if czy_jednomasztowiec(plansza , i , n + 1 - i):
            jednomasztowiec += 1
        if czy_dwumasztowiec(plansza , i ,  n - i + 1) and (i , n - i + 1) not in odwiedzone:
            dwumasztowiec += 1
            for x in range(i-1 , i+2):
                for y in range(i-1 , n - 1 + 1 +2):
                    odwiedzone.add((x,y))



    return jednomasztowiec , dwumasztowiec

wynik1 , wynik2 = po_przekatnej(plansza)

zapis.write(str(wynik1) + ' ' + str(wynik2))

plik.close()
zapis.close()
