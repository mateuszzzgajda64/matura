n = int(input())

def usuwanieSpacji(key):
    nowy = ''
    for i in key:
        if i != ' ':
            nowy = nowy + i
    return nowy

dane = {}

for i in range(n):
    klucz = input()
    key = usuwanieSpacji(klucz)
    wartosc = input()
    dane[key] = wartosc

for key , wartosc in dane.items():
    print(f'{key}: {wartosc}')

