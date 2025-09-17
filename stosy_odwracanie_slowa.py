def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

napis = 'lubie stosy'

def odwrocenieNapisu(napis):
    stos = []
    odwrocony = ''
    for i in range(len(napis)):
        push(stos, napis[i])
    for i in range(len(napis)):
        odwrocony = odwrocony + peek(stos)
        pop(stos)
    return odwrocony

print(odwrocenieNapisu(napis))
