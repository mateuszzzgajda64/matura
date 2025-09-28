def push(stos , wartosc):
    stos.append(wartosc)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[-1]

def isEmpty(stos):
    return len(stos)==0

def usuwanieHashtaga(wyraz):
    stos = []
    for znak in wyraz:
        if znak == '#':
            if not isEmpty(stos):
                pop(stos)
        else:
            push(stos, znak)
    return stos

def logi(wyraz1 , wyraz2):
    return usuwanieHashtaga(wyraz1) == usuwanieHashtaga(wyraz2)

wyraz1 = str(input())
wyraz2 = str(input())


if logi(wyraz1, wyraz2):
    print('Ciągi znaków są identyczne.')
else:
    print('Ciągi znaków nie są identyczne.')
