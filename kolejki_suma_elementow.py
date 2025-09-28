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

def suma(q):
    suma = 0
    while not isEmpty(q):
        suma = suma + pop(q)
    return suma

q = []
n = int(input())
for i in range(n):
    push(q , int(input()))

suma1 = suma(q)

print(suma1)

