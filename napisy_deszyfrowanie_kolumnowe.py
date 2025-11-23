def szyfrowanieKolumnowe(tekst , klucz):
    matrix = []
    a = 0

    for i in range(klucz):
        matrix.append([])
        for j in range(klucz):
            matrix[i].append('')

    for j in range(klucz):
        for i in range(klucz):
            if a < len(tekst):
                matrix[i][j] = tekst[a]
                a += 1

    wynik = ''
    for i in range(klucz):
        for j in range(klucz):
            if matrix[i][j] != 'X':
                wynik += matrix[i][j]
    return wynik


tekst = str(input())
klucz = int(input())
szyfrogram = szyfrowanieKolumnowe(tekst, klucz)

print(szyfrogram)
