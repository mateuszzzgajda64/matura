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

def czyZaakceptowano():
    return random.randint(0 , 3) == 0


q = []
n = int(input())

for i in range(n):
    imie = input()
    push(q, imie)

nrklienta = 1
while not isEmpty(q):
    if czyZaakceptowano():
        print(f'{nrklienta}: {front(q)} - dokumenty zaakceptowane')
        pop(q)
    else:
        print(f'{nrklienta}: {front(q)} - dokumenty niezaakceptowane')
        push(q, front(q))
        pop(q)
    nrklienta += 1


