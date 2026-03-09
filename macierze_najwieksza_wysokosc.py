plik = open('macierz.txt' , 'r')
zapis = open('wynik1' , 'w')

macierz = []

licznik_maksimow = 0
max_h = -1
top_i = 0
top_j = 0
top_wartosc = 0

for linia in plik:
    linia = list(linia.strip().split(' '))

    macierz.append(linia)

for i in range(1 , len(macierz) - 1):
    for j in range(1 , len(macierz[i]) - 1):

        a = int(macierz[i][j])

        gora = int(macierz[i-1][j])
        dol = int(macierz[i+1][j])
        lewo = int(macierz[i][j - 1])
        prawo = int(macierz[i][j+1])

        if a > gora and a > dol and a > lewo and a > prawo:
            licznik_maksimow += 1
            najmniejsza = (min(gora , dol, lewo, prawo))
            roznica = a - najmniejsza
            if roznica > max_h:
                max_h = roznica
                top_i = i
                top_j = j
                top_wartosc = a

print(licznik_maksimow)
print(max_h)
print(top_i +1, top_j+1)
