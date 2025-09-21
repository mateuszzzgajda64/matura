def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def zagniezdzenie(nawiasy):
    stos = []
    pary = {')' : '(' , ']': '[' , '}' : '{'}
    for znak in nawiasy:
        if znak == '(' or znak == '[' or znak == '{':
            push(stos, znak)
        elif znak == ')' or znak == ']' or znak == '}':
            if isEmpty(stos):
                return False
            if pop(stos) != pary[znak]:
                return False
    return isEmpty(stos)

ciag = str(input())

if zagniezdzenie(ciag):
    print('Nawiasy są poprawnie zagnieżdżone.')
else:
    print('Nawiasy nie są poprawnie zagnieżdżone.')
