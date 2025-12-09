system = int(input())
n = str(input())

def konwertuj(system , a):
    wynik = 0
    for i in range(len(a)):
        potega = len(a) - i - 1
        czynnik = a[i]
        if '0' <= czynnik <= '9':
            czynnik = int(czynnik)
            wynik = wynik + (int(system**potega) * int(czynnik))
        elif 'A' <= czynnik <= 'Z':
            czynnik = int(ord(czynnik) - 55)
            wynik = wynik + (int(system ** potega) * int(czynnik))
    return wynik

print(konwertuj(system , n))
