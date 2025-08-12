n = int(input())
m = int(input())
macierz = []

def sumaLiter(slowo):
    suma = 0
    for litera in range(len(slowo)):
        suma = suma + ord(slowo[litera])
    return suma

def czyWiekszeOd500(slowo):
    if sumaLiter(slowo) > 500:
        return True
    return False

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(str(input()))
    macierz.append(wiersz)

for i in range(n):
    for j in range(m):
        if czyWiekszeOd500(macierz[i][j]):
            print(macierz[i][j])
