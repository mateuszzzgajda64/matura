plik = open('dane4.txt' , 'r')
zapis = open("wynik6.txt", "w")

def czyPierwsza(a):
    if a < 2:
        return False
    for i in range(2 , a):
        if a % i == 0:
            return False
    return True

tab = []

for linia in plik:
    liczba = int(linia.strip())
    pierwsza = czyPierwsza(liczba)
    if pierwsza == True:
        tab.append(liczba)

najwieksza = max(tab)
najmniejsza = min(tab)

zapis.write(f'Najwieksza: {najwieksza}\nNajmniejsza: {najmniejsza}')
plik.close()
zapis.close()
