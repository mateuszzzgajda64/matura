import random
def push(q , wartosc):
    q.append(wartosc)
    return q

def pop(q):
    return q.pop(0)

def front(q):
    return q[0]

def back(q):
    return q[-1]

def isEmpty(q):
    return len(q) == 0

def size(q):
    return len(q)

def czyPalindrom(slowo):
    odwrocone = slowo[::-1]
    q1 = []
    q2 = []
    for i in range(len(slowo)):
        push(q1, slowo[i])
    for i in range(len(odwrocone)):
        push(q2, odwrocone[i])
    palindrom = True

    while not isEmpty(q1):
        if front(q1) == front(q2):
            palindrom = True
            pop(q1)
            pop(q2)
        else:
            palindrom = False
            break
    return palindrom

slowo = str(input())

if czyPalindrom(slowo):
    print('Napis jest palindromem.')
else:
    print('Napis nie jest palindromem.')

