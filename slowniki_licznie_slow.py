zdanie = input()

def duzeNaMale(zdanie):
    nowe = ''
    for litera in zdanie:
        if 'A' <= litera <= 'Z':
            nowe = nowe + chr(ord(litera) + 32)
        else:
            nowe = nowe + litera
    return nowe

def slowaDoTablicy(zdanie):
    tab = []
    slowo = ''
    for litera in zdanie:
        if litera != ' ':
            slowo += litera
        else:
            if slowo:
                tab.append(slowo)
                slowo = ''
    if slowo:
        tab.append(slowo)
    return tab

nowezdanie = duzeNaMale(zdanie)
arr = slowaDoTablicy(nowezdanie)
slownik = {}
for slowo in arr:
    if slowo in slownik:
        slownik[slowo] += 1
    else:
        slownik[slowo] = 1

najczestrze = ''
najwieksza = 0

for slowo in slownik:
    if slownik[slowo] > najwieksza:
        najwieksza = slownik[slowo]
        najczestrze = slowo

print(najczestrze , najwieksza)
