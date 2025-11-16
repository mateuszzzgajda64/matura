napis = str(input())
klucz = int(input())

def cezarOdkoduj(napis, klucz):
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

def cezarZakoduj(napis, klucz):
    klucz = klucz % 26
    szyfr = ''
    for i in napis:
        if 'A' <= i <= 'Z':
            szyfr = szyfr + chr((ord(i) - ord('A') + klucz) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            szyfr = szyfr + chr((ord(i) - ord('a') + klucz) % 26 + ord('a'))
        else:
            szyfr = szyfr + i
    return szyfr
