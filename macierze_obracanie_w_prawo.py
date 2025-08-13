n = int(input())
m = int(input())
macierz = []

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(str(input()))
    macierz.append(wiersz)

macierzpom = []

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(0)
    macierzpom.append(wiersz)

for i in range(n):
    for j in range(m):
        print(macierz[i][j] , end=' ')
    print()
print()

for i in range(n):
    for j in range(m):
        macierzpom[j][n - i  - 1] = macierz[i][j]

for i in range(n):
    for j in range(m):
        print(macierzpom[i][j] , end=' ')
    print()
print()
