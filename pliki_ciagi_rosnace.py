plik = open('cyfry.txt' , 'r')
zapis = open("zadanie4.txt", "w")

for linia in plik:
    liczba = linia.strip()
    ciag = True
    for i in range(len(liczba) - 1) :
        if int(liczba[i]) >= int(liczba[i + 1]):
            ciag = False
            break
    if ciag:
        zapis.write(f'{liczba}\n')

plik.close()
zapis.close()
