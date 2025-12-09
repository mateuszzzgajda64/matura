n = int(input())

def konwertuj(a):
    wynik = ''
    while a > 0:
        if a % 2 == 0:
            wynik = wynik + '0'
            a = a // 2
        elif a % 2 == 1:
            wynik = wynik + '1'
            a = a // 2
    return wynik[::-1]

print(konwertuj(n))

