plik = open('hasla.txt' , 'r')
zapis = open("wynik4a.txt", "w")

parzyste = 0
nieparzyste = 0
for linia in plik:
    tekst = linia.strip()
    n = len(tekst)
    if n % 2 == 0:
        parzyste = parzyste + 1
    else:
        nieparzyste = nieparzyste + 1

zapis.write(f'Parzyste: {parzyste}\nNieparzyste: {nieparzyste}')

plik.close()
zapis.close()

