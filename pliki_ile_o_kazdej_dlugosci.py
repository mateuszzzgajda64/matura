plik = open('napisy.txt' , 'r')
zapis = open("zadanie4.txt", "w")

tab = [0]*17

for linia in plik:
    tekst = linia.strip()
    n = len(tekst)
    if 2 <= n <= 16:
        tab[n] = tab[n] + 1

for i in range(2 , 17):
    zapis.write(f'{i} {tab[i]}\n')


plik.close()
zapis.close()
