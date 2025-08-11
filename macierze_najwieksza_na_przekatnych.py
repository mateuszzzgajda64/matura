n = int(input())

macierz = []

for i in range(n):
    wiersz = []
    for j in range(n):
        wiersz.append(int(input()))
    macierz.append(wiersz)

najwieksza = macierz[0][0]
for i in range(n):
    if macierz[i][i] >= najwieksza:
        najwieksza = macierz[i][i]

for i in range(n - 1 , -1 , -1):
    if macierz[i][n - 1 - i] >= najwieksza:
        najwieksza = macierz[i][n - 1 - i]

print(najwieksza)
