n = 3

def stworz(n ):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for i in macierz:
        print(*i)

def wyznacznik(macierz):
    w = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) + matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
    return w

matrix = stworz(n)
print(wyznacznik(matrix))
