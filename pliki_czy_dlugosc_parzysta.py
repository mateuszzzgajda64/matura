plik = open('napisy.txt' , 'r')
zapis = open("zadanie4.txt", "w")
licznik = 0
for linia in plik:
    napis = linia.strip()
    if len(napis) % 2 == 0:
        licznik = licznik + 1

zapis.write(f'{licznik}')


plik.close()
zapis.close()
