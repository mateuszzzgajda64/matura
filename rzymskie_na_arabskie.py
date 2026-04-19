m = []
n = int(input())

def RzymskieNaArabskie(a):
    znaki = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    wynik = 0

    for i in range(len(a)):
        if i + 1 < len(a) and znaki[a[i + 1]] > znaki[a[i]]:
            wynik = wynik - znaki[a[i]]
        else:
            wynik = wynik + znaki[a[i]]

    return wynik


for i in range(n):
    w = []
    for j in range(n):
        w.append(str(input()))
    m.append(w)
symbole = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

mx = []
for i in m:
    wiersz = []
    for j in i:
        if all(k in symbole for k in j):
            wiersz.append(int(RzymskieNaArabskie(j)))
        else:
            wiersz.append(int(j))
    mx.append(wiersz)

suma = 0
for i in range(len(mx)):
    suma = suma + mx[i][i]

for i in range(len(mx)):
    suma = suma + mx[i][len(mx[i]) - i - 1]

if len(mx) % 2 == 1:
    suma = suma - mx[len(mx)//2][len(mx)//2]

print(suma)



