# NWW mozna liczyc z A*B/NWD(A , B)

n = int(input())
m = int(input())

def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def NWW(a, b):
    nww = int(a*b/NWD(a, b))
    return nww

print(NWW(n, m))
