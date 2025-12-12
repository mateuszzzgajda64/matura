a = str(input())
b = str(input())
podstawa = int(input())

def intNaChar(liczba):
    if liczba >= 10:
        return chr(55 + liczba)
    return str(liczba)

def charNaInt(znak):
    if 'A' <= znak <= 'Z':
        return ord(znak) - 55
    return int(znak)

def dodaj_zera(liczba , zera):
    wynik = liczba
    for i in range(zera):
        wynik = '0' + wynik
    return wynik

def dodawanie_binarne(a , b , podstawa):
    wynik = ''
    if len(a) > len(b):
        roznica = len(a) - len(b)
        b = dodaj_zera(b, roznica)
    if len(a) < len(b):
        roznica = len(b) - len(a)
        a = dodaj_zera(a, roznica)

    przeniesienie = 0
    for i in range(len(b) - 1 , -1, -1):
        suma = przeniesienie
        suma = suma + charNaInt(a[i])
        suma = suma + charNaInt(b[i])

        if suma >= podstawa:
            przeniesienie = 1
            suma = suma - podstawa
        else:
            przeniesienie = 0
        wynik = intNaChar(suma) + wynik
        if i == 0 and przeniesienie > 0:
            wynik = intNaChar(przeniesienie) + wynik
    return wynik

print(dodawanie_binarne(a , b , podstawa))
