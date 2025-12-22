napis = ' Ala ma KOTA '
print(napis.capitalize())
print(napis.upper())
print(napis.lower())
print(napis.title())
print(napis.swapcase())
print(napis.strip()) #usuwa spacje przed i po napisie
print(napis.isalpha())
print(napis.isdigit())
print(napis.isalnum()) #litery lub cyfry
print(napis.isspace()) # czy zawiera tylko biale znaki
print(napis.count('A'))
print(napis.startswith('A')) # napis zaczyna sie na
print(napis.endswith('A')) # napis konczy sie na
print(napis.replace('A', 'B'))
print(napis.replace('A', 'B', 1)) # raz zamienia
print(napis.find('m'))

napis2 = 'Ala , ma , kota'
print(napis2.split(' , '))a

napis3 = '7'
print(napis3.zfill(3)) # dorzuca zera na poczatek aby osiagnac wpisana dlugosc
