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

def czyIdentyczne(q1 , q2):
    identyczna = True
    if size(q1) != size(q2):
        identyczna = False
    while not isEmpty(q1):
        liczba1 = pop(q1)
        liczba2 = pop(q2)
        if liczba1 == liczba2:
            identyczna = True
        else:
            identyczna = False
    return identyczna

n = int(input())

print('podaj pierwsza kolejke')
q1 = []
for i in range(n):
    push(q1 , int(input()))

print('podaj druga kolejke')
q2 = []
for i in range(n):
    push(q2 , int(input()))

print(czyIdentyczne(q1, q2))
