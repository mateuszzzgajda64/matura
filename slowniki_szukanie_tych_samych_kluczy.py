n = int(input())

slownik1 = {}
slownik2 = {}

for i in range(n):
    klucz = input()
    wartosc = input()
    slownik1[klucz] = wartosc

m = int(input())

for i in range(m):
    klucz = input()
    wartosc = input()
    slownik2[klucz] = wartosc

for klucz in slownik1:
    if klucz in slownik2:
        print(klucz)
