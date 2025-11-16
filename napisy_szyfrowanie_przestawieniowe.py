napis = str(input())

def szyfruj(slowo):
    tab = list(slowo)
    for i in range(0 , len(tab) -1 , 2):
        tab[i] , tab[i + 1] = tab[i + 1], tab[i]
    return tab

wynik = ''
slowo = szyfruj(napis)
for i in range(len(slowo)):
    wynik += slowo[i]

print(wynik)

#ODSZYFROWANIE DZIALA DOKLADNIE TAK SAMO BO TRTZEBA NA NOWO ZAMIENIC LITERY MIEJSCAMI I BAJLANDO
