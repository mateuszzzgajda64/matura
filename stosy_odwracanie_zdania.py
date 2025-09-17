def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def odwroc(stos):
    odwrocone = ''
    while not isEmpty(stos):
        s = peek(stos)
        odwrocone  = odwrocone + s + ' '
        pop(stos)
    return odwrocone

zdanie = str(input())

tab = zdanie.split()

stos = []
for i in range(len(tab)):
    push(stos, tab[i])

print(odwroc(stos))
