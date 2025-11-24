def szybkiepotegowanie(a , b):
    wynik = 1
    while b > 0:
        if b % 2 == 1:
            wynik = wynik * a
        a = a * a
        b = b // 2
    return wynik

a = int(input())
b = int(input())
print(szybkiepotegowanie(a,b))
