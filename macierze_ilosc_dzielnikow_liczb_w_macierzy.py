n = int(input())
m = int(input())

def stworzMacierz(n , m):
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def wypiszMacierz(macierz):
    for i in macierz:
        print(*i)

def podajIloscDzielnikow(liczba):
    licznik = 0
    for i in range(1 , liczba + 1 , 1):
        if liczba % i == 0:
            licznik = licznik + 1
    return licznik

def wypiszDzielniki(macierz):
    matrix = []
    for i in range(len(macierz)):
        wiersz = []
        for j in range(len(macierz[i])):
            wiersz.append(podajIloscDzielnikow(macierz[i][j]))
        matrix.append(wiersz)
    return matrix

wygenerowana = stworzMacierz(n , m)
macierzdzielnikow = wypiszDzielniki(wygenerowana)

wypiszMacierz(macierzdzielnikow)
