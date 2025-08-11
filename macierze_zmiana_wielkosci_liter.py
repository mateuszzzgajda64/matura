n = int(input())
m = int(input())

macierz = []

def maleNaDuze(a):
    if 64 < ord(a) < 91:
        nowy = ord(a) + 32
        b = chr(nowy)
        return b
    else:
        return a

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(str(input()))
    macierz.append(wiersz)

for i in range(n):
    for j in range(m):
        print(maleNaDuze(macierz[i][j]) , end=' ')
    print()

