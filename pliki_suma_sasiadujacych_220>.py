plik = open('hasla.txt' , 'r')
zapis = open("wynik4c.txt", "w")

for linia in plik:
    tekst = linia.strip()
    for i in range(len(tekst) - 1):
        if ord(tekst[i]) + ord(tekst[i + 1]) == 220:
            zapis.write(f'{tekst}\n')
            break

plik.close()
zapis.close()
