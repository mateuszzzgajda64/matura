n = int(input())

tab = []

for i in range(n):
    tab.append(str(input()))

slownik1 = {}

for slowo in tab:
    klucz = slowo[0]
    if klucz not in slownik1:
        slownik1[klucz] = []
    slownik1[klucz].append(slowo)

for k , v in slownik1.items():
    print(k, ': ', v)

