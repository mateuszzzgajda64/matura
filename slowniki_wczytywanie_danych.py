n = int(input())

osoba = {}

for i in range(n):
    klucz = input()
    wartosc = input()
    osoba[klucz] = wartosc

for klucz , wartosc in osoba.items():
    print(f'{wartosc} -> {klucz}')
