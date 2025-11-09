n = int(input())

tab = []

for i in range(n):
    liczba = int(input())
    tab.append(liczba)

def sortowanie(tab):
    d = len(tab)
    for i in range(d - 1):
        index = i
        for j in range(i + 1, d):
            if tab[index] > tab[j]:
                index = j
        tab[index ] , tab[i] = tab[i], tab[index]

    return tab

print(sortowanie(tab))
