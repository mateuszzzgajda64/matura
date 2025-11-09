a = int(input())
b = int(input())

def NWD(a, b):
    while b > 0:
        reszta = a % b
        a = b
        b = reszta
        if b == 0:
            break
    return a
print(NWD(a, b))
