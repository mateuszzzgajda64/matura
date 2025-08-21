def maximum(A):
    najwieksza = A[0]
    for i in range(len(A)):
        if A[i] > najwieksza:
            najwieksza = A[i]
    return najwieksza
def minimum(A):
    najmniejsza = A[0]
    for i in range(len(A)):
        if A[i] < najmniejsza:
            najmniejsza = A[i]
    return najmniejsza

plik = open('cyfry.txt' , 'r')
zapis = open("zadanie4.txt", "w")
sumy = []
liczby = []
for linia in plik:
    tekst = linia.strip()
    liczby.append(tekst)
    suma = 0
    for i in range(len(tekst)):
        suma = int(tekst[i]) + suma
    sumy.append(suma)

najw = maximum(sumy)
najmn = minimum(sumy)

najwiekszaliczba = liczby[sumy.index(najw)]
najmniejszaliczba = liczby[sumy.index(najmn)]

zapis.write(f'Liczba z najwieksza suma cyfr:{najwiekszaliczba}\n')
zapis.write(f'Liczba z najmniejsza suma cyfr:{najmniejszaliczba}')

plik.close()
zapis.close()
