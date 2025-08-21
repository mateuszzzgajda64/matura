plik = open('cyfry.txt' , 'r')
zapis = open("zadanie4.txt", "w")
licznik = 0
for linia in plik:
    tekst = linia.strip()
    if int(linia) % 2 == 0:
        licznik = licznik + 1
zapis.write(f'{licznik}\n')


plik.close()
zapis.close()
