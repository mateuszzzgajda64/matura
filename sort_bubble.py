n = int(input())

tab = []

for i in range(n):
    liczba = int(input())
    tab.append(liczba)

def sortowanie(tab):
    for i in range(len(tab) - 1):
        zamiana = False
        for j in range(1 , len(tab) - i):
            if tab[j-1] < tab[j]:
                tab[j-1], tab[j] = tab[j], tab[j-1]
                zamiana = True
        if not zamiana:
            break
    return tab

print(sortowanie(tab))
