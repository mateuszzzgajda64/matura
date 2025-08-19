
def stworz(a , b):
    macierz = []
    for i in range(a):
        wiersz = []
        for j in range(b):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for i in macierz:
        print(*i)

def iloczyn(A , B):
    macierzpom = []
    for i in range(n):
        wiersz = []
        for j in range(q):
            wiersz.append(0)
        macierzpom.append(wiersz)

    if m != p:
        return 0

    for i in range(n):
        for j in range(q):
            for k in range(m):
                macierzpom[i][j] = A[i][k] * B[k][j] + macierzpom[i][j]
    return macierzpom

n = int(input())
m = int(input())
matrix = stworz(n , m)


p = int(input())
q = int(input())
matrix2 = stworz(p , q)


matrix3 = iloczyn(matrix , matrix2)
wypisz(matrix3)

