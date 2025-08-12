n = int(input())
m = int(input())
macierz = []

def czySamogloska(litera):
    samogloski = 'aeiouyAEIOUY'
    return litera in samogloski

def ileSamolosek(slowo):
    licznik = 0
    for litera in slowo:
        if czySamogloska(litera):
            licznik = licznik + 1
    return licznik

for i in range(n):
    wiersz = []
    for j in range(m):
        wiersz.append(str(input()))
    macierz.append(wiersz)

najwieksza = ileSamolosek(macierz[0][0])
pom = macierz[0][0]
for i in range(n):
    for j in range(m):
        if najwieksza < ileSamolosek(macierz[i][j]):
            najwieksza = ileSamolosek(macierz[i][j])
            pom = macierz[i][j]          
print(pom)

