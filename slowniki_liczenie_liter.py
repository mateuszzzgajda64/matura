n = input()
slownik1 = {}

def liczLitery(slowo):
    slownik = {}
    for litera in slowo:
        if litera in slownik and litera != ' ':
            slownik[litera] += 1
        if litera not in slownik and litera != ' ':
            slownik[litera] = 1
    return slownik

nowy = liczLitery(n)

for k , v in nowy.items():
    print(f"{k}: {v}")
