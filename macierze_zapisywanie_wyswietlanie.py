n = int(input())
m = int(input())

# liczba = int(input())

macierz = []

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(int(input()))
    macierz.append(wiersz)

for i in range(n):
    for j in range(m):
        print(macierz[i][j] , end=' ')
    print()
