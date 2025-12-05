plik = open("liczby_hex.txt","r")
zapis = open("wyniki_hex.txt","w")

def czyPierwsza(x):
    if x < 2:
        return False
    for i in range(2 , int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def znaknaliczba(a):
    a = str(a)
    if 'A' <= a <= 'F':
        a = int(ord(a) - 55)
    return int(a)

def hexnadec(a):
    a = str(a)
    suma = 0
    for i in range(len(a)):
        potega = len(a) - i - 1
        suma = suma + int(znaknaliczba(a[i]))* (16**potega)
    return suma
tab = []
for line in plik:
    a = line.strip()
    a = str(a)
    tab.append(hexnadec(a))

licznik = 0
for i in range(len(tab)):
    if czyPierwsza(tab[i]):
        licznik = licznik + 1

zapis.write(str(licznik) + "\n")
plik.close()
zapis.close()
