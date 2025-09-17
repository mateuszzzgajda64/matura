def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def zagniezdzenie(nawiasy):
    stos = []
    glebokosc = 0
    maxymalna = 0
    for znak in nawiasy:
        if znak == '(':
            push(stos , '(')
            glebokosc = glebokosc + 1
            if glebokosc > maxymalna:
                maxymalna = glebokosc
        elif znak == ')':
            if isEmpty(stos):
                return False
            pop(stos)
            glebokosc = glebokosc - 1
    if not isEmpty(stos):
        return False

    return maxymalna

ciag = str(input())

print(zagniezdzenie(ciag))
