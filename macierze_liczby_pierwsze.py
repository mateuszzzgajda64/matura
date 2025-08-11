n = int(input())
m = int(input())

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
    for j in range(m):
        wiersz.append(int(input()))
    macierz.append(wiersz)

for i in range(n):
    for j in range(m):
        if czyPierwsza(macierz[i][j]):
            print(macierz[i][j])
