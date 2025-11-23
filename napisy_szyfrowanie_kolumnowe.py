def szyfrowanieKolumnowe(tekst , klucz):
    matrix = []
    a = 0
    for i in range(klucz):
        matrix.append([])
        for j in range(klucz):
            if a < len(tekst):
                matrix[i].append(tekst[a])
                a += 1
            else:
                matrix[i].append('X')
    szyfrogram = ''
    for i in range(klucz):
        for j in range(klucz):
            szyfrogram += matrix[j][i]

    for i in range(klucz):
        for j in range(klucz):
            print(matrix[i][j] , end = '')
        print()

    return szyfrogram

tekst = 'tojestprzykladowytekst'
klucz = 5
szyfrogram = szyfrowanieKolumnowe(tekst, klucz)

print(szyfrogram)
