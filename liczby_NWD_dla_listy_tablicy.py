n = int(input())

tab = []

for i in range(n):
    tab.append(int(input()))

def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def NWDdlaListy(tab):
    wynik = tab[0]
    for i in range(1, len(tab)):
        wynik = NWD(wynik, tab[i])
    return wynik

print(NWDdlaListy(tab))
