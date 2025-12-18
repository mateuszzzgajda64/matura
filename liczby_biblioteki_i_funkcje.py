import math
import random

zaokraglanie = round(4567812345 , -7)
print(zaokraglanie)

bezwgledna = abs(-10)
print(bezwgledna)

dzielenieZreszta = divmod(9 , 2)
print(dzielenieZreszta) # odpowiedz jako krotka

potegowanie = pow(2 , 10) # mozemy dodac trzeci argument ktory bedzie robil modulo
print(potegowanie)

liczba = int(1.27) # zamienia na inty wszytko
print(liczba)

prawdaczyfalsz = bool(4 < 5)
print(prawdaczyfalsz)

przecinki = float(3 / 4)
print(przecinki)

czyString = isinstance('fueeh' , str)
zmienna = {}
czydict = isinstance(zmienna, dict)
print(czyString)
print(czydict)

dziesietnyNaBinarny = bin(7)
dziesietnyNaHexalny = hex(20)
print(dziesietnyNaBinarny) # 0b oznacza binarny , 0x - hexalny , 0o - oktalny
print(dziesietnyNaHexalny)

hexalnyNaDziesietny = int('AA' , 16)
print(hexalnyNaDziesietny)

print(math.floor(3.99)) #zaokraglanie w dol
print(math.ceil(3.11)) # zaokraglanie w gore

print(math.sqrt(64))

print(math.factorial(5))

print(random.randint(1,100))




