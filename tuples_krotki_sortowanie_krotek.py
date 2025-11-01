n = int(input())

krotki = []

for i in range(n):
    imie = str(input())
    liczba = int(input())
    krotki.append((imie, liczba))

def sortujKrotki(krotki):
    return sorted(krotki) , list(sorted(krotki, key = lambda x: x[1]))

posortowane = sortujKrotki(krotki)
print(posortowane)
