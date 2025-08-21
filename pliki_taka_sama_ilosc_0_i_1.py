plik = open('napisy.txt' , 'r')
zapis = open("zadanie4.txt", "w")

licznik  = 0
for linia in plik:
    licznik0 = 0
    licznik1 = 0
    napis = linia.strip()
    for i in range(len(napis)):
        if int(napis[i]) ==0:
            licznik0 = licznik0 + 1
        elif int(napis[i]) == 1:
            licznik1 = licznik1 + 1
    if licznik1 == licznik0:
        licznik = licznik + 1

zapis.write(f'{licznik}')


plik.close()
zapis.close()
