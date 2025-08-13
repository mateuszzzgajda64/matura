n = int(input())
m = int(input())
macierz = []

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(int(input()))
    macierz.append(wiersz)

macierzpom = []

for i in range(m):
    wiersz = []
    for j in range(n):
        wiersz.append(0)
    macierzpom.append(wiersz)

for i in range(m):
    for j in range(n):
        macierzpom[i][j] = macierz[j][i]

for i in range(m):
    for j in range(n):
        print(macierzpom[i][j] , end=' ')
    print()
