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

def znajdzZnaki(slowo):
    slownik = {}

    q = []
    for i in range(len(slowo)):
        push(q , slowo[i])

    while not isEmpty(q):
        if front(q) not in slownik:
            wartosc = front(q)
            slownik[wartosc] = 1
            pop(q)
        else:
            slownik[front(q)] += 1
            pop(q)
    return slownik

slowo = str(input())

slownik = znajdzZnaki(slowo)

for k , v in slownik.items():
    if v < 2:
        print(k)
        break
else:
    print(-1)
