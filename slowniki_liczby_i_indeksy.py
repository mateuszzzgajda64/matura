n = int(input())

slownik = {}
arr = []

for i in range(n):
    arr.append(input())


def indeksy(tab):
    slownik = {}
    for i in range(len(tab)):
        liczba = tab[i]
        slownik[liczba] = []
        for j in range(len(tab)):
            if tab[j] == liczba:
                slownik[liczba].append(j)
    return slownik

slownik1 = indeksy(arr)
for k , v in slownik1.items():
    print(f"{k}: {v}")
