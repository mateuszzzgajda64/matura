n = int(input())
m = int(input())

def stworz(n , m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def transponowana(n , m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0)
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for i in macierz:
        print(*i)

def transponuj(macierz , macierzpom):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            macierzpom[i][j] = macierz[j][i]
    return macierzpom

def czy_symetryczna(A):
    if n != m:
        return False
    if A == transponuj(matrix , matrixT):
        return True
    else:
        return False

matrix = stworz(n , m)
matrixT = transponowana(n , m)

print(czy_symetryczna(matrix))
