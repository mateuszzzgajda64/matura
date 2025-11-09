n = int(input())

tab = []

for i in range(n):
    liczba = int(input())
    tab.append(liczba)

def sortowanie(tab):
    d = len(tab)
    for i in range(1 , d):
        wstawiana = tab[i]
        j = i  -1
        while j >= 0 and tab[j] > wstawiana:
            tab[j+1] = tab[j]
            j = j - 1
        tab[j+1] = wstawiana
    return tab

print(sortowanie(tab))
