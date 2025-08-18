n = int(input())
m = int(input())
macierz = []
macierz2 = []

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(int(input()))
    macierz.append(wiersz)

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(int(input()))
    macierz2.append(wiersz)

def dodaj_macierze(A, B):
    matrix = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(A[i][j] + B[i][j])
        matrix.append(wiersz)
    return matrix

wynik = dodaj_macierze(macierz, macierz2)
for i in range(n):
    for j in range(m):
        print(wynik[i][j], end=' ')
    print()
