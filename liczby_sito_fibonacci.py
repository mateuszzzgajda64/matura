def sito(liczba):
    maksdzielnik = int(liczba ** 0.5)
    liczby = []
    for i in range(2 , liczba):
        liczby.append(i)

    for dzielnik in range(2 , maksdzielnik + 1):
            for i in range(0 , len(liczby)):
                if liczby[i] % dzielnik == 0 and liczby[i] != 0 and liczby[i] != dzielnik:
                    liczby[i] = 0
    return(liczby)

def kasujZera(tab):
    arr = []
    for i in range (len(tab)):
        if tab[i] != 0:
            arr.append(tab[i])
    return arr


def fibo(n):
    tab = [1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        tab.append(b)
    return tab


n = int(input())

maxfibo = max(fibo(n))
tab = fibo(n)
arr = kasujZera(sito(maxfibo))

wynik = []
for i in tab:
    if i in arr:
        wynik.append(i)

print(wynik)
