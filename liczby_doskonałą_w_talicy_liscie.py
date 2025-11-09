n = int(input())
m = int(input())
arr = []

for i in range(n , m + 1):
    arr.append(i)

def dzielniki(a):
    tab = []
    for i in range(1 , a):
        if a % i == 0:
            tab.append(i)
    return tab
def czyDoskonala(a):
    if sum(dzielniki(a)) == a:
        return True
    else:
        return False

wynik = []
for i in range(1 , len(arr)):
    if czyDoskonala(i):
        wynik.append(i)

print(wynik)
