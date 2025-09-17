def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def generujStos(n):
    wygeneruj = []
    for i in range(1 , n + 1):
        push(wygeneruj, i)
    return wygeneruj

def wypiszStos(stos):
    while not isEmpty(stos):
        print(peek(stos))
        pop(stos)

stos = []

push(stos, 1)
push(stos, 2)
push(stos, 3)
push(stos, 4)
push(stos, 5)

