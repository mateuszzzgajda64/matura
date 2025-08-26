plik = open('liczby1.txt' , 'r')
zapis = open("wynik5.txt", "w")

tab = []
odwiedzone = []
wynik = []

for linia in plik:
    liczba = int(linia.strip())
    tab.append(liczba)

licznikmax = 0
najczesciejwystepujaca = ''

for i in range(len(tab)):
    slowo = tab[i]
    if slowo in odwiedzone:
        continue
    odwiedzone.append(slowo)

    licznik = 0

    for j in range(len(tab)):
        if slowo == tab[j]:
            licznik = licznik + 1

    wynik.append((slowo , licznik))

    if licznik > licznikmax:
        licznikmax = licznik
        najczesciejwystepujaca = slowo

zapis.write(f'Liczba występująca najczęściej: {najczesciejwystepujaca}\n')
for slowo , licznik in sorted(wynik):
    zapis.write(f'{slowo} {licznik}\n')

plik.close()
zapis.close()
