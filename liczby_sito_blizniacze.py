def sito(liczba):
    maksdzielnik = int(liczba ** 0.5)
    liczby = []
    for i in range(2 , n):
        liczby.append(i)

    for dzielnik in range(2 , maksdzielnik + 1):
            for i in range(0 , n - 2):
                if liczby[i] % dzielnik == 0 and liczby[i] != 0 and liczby[i] != dzielnik:
                    liczby[i] = 0
    return(liczby)

def kasujZera(tab):
    arr = []
    for i in range (len(tab)):
        if tab[i] != 0:
            arr.append(tab[i])
    return arr

def blizniacze(tab):
    arr = []
    for i in range (len(tab) - 1): ## -1 !!!!!
        if tab[i + 1] - tab[i] == 2:
            arr.append((tab[i] , tab[i + 1]))

    return arr

n = int(input())

tab = sito(n)
tab = kasujZera(tab)
arr = blizniacze(tab)
print(arr)
