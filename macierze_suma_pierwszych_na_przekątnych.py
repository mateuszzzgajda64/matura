n = int(input())

macierz = []

def czyPierwsza(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

for i in range(n):
    wiersz = []
    for j in range(n):
        wiersz.append(int(input()))
    macierz.append(wiersz)

suma = 0

for i in range(n):
    if czyPierwsza(macierz[i][i]):
        suma = macierz[i][i] + suma

for i in range(n - 1 , -1 , -1):
    if czyPierwsza(macierz[n - 1 - i][i]):
        suma = macierz[n - 1 - i][i] + suma

print(suma)
