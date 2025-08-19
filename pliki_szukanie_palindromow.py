plik = open('./dane.txt' , 'r')

for linia in plik:
    tekst = linia.strip()
    if tekst == tekst[::-1]:
        print(tekst)

plik.close()
