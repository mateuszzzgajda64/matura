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

q = []
n = int(input())

for i in range(n):
    klient={
        'imie': input(),
        'nazwisko': input(),
    }
    push(q, klient)

while not isEmpty(q):
    print(f'{front(q)['imie']} {front(q)['nazwisko']}')
    pop(q)
