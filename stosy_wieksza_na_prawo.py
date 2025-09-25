def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def wieksza(tab):
    n = len(tab)
    slownik = {}
    stos = []
    for i in range(n - 1 , -1 , -1):
        while not isEmpty(stos) and peek(stos) <= tab[i]:
            pop(stos)
        if isEmpty(stos):
            slownik[tab[i]] = -1
        else:
            slownik[tab[i]] = peek(stos)
        push(stos, tab[i])
    return slownik

n = int(input())

tab = []

for i in range(n):
    a = int(input())
    push(tab, a)

slownik1 = wieksza(tab)

for v in tab:
    print(f'{v} -> {slownik1[v]}')
