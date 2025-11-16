napis = str(input())

def znajdzNajwiekszaIloscLitera(napis):
    slownik = {}
    licznik = 0
    for i in napis:
        if i in slownik and i != ' ':
            slownik[i] = slownik[i] + 1
        if i not in slownik and i != ' ':
            slownik[i] = 1
    maxklucz = None
    maxwartosc = -1

    for k in slownik:
        if slownik[k] > maxwartosc:
            maxwartosc = slownik[k]
            maxklucz = k
    return maxklucz

def szukanieKlucza(litera):
    if 'A' <= litera <= 'Z':
        key = ord(litera) - ord('A')
    if 'a' <= litera <= 'z':
        key = ord(litera) - ord('a')
    return key

def cezar(napis, klucz):
    klucz = klucz % 26
    szyfr = ''
    for i in napis:
        if 'A' <= i <= 'Z':
            szyfr = szyfr + chr((ord(i) - ord('A') - klucz) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            szyfr = szyfr + chr((ord(i) - ord('a') - klucz) % 26 + ord('a'))
        else:
            szyfr = szyfr + i
    return szyfr

litera = str(znajdzNajwiekszaIloscLitera(napis))
klucz = szukanieKlucza(litera)

print(cezar(napis, klucz))
