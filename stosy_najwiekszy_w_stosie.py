def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def najwiekszyWStosie(stos):
    najwiekszy = peek(stos)
    while not isEmpty(stos):
        wartosc = peek(stos)
        if najwiekszy < wartosc:
            najwiekszy = wartosc
        pop(stos)
    return najwiekszy

n = int (input ())
stos = []
for i in range(n):
    wartosc = int(input())
    push(stos, wartosc)

print(najwiekszyWStosie(stos))
