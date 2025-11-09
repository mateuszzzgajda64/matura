a = int(input())
b = int(input())

def NWD(a, b):
    if b == 0:
        return a
    return NWD(b , a % b)

print(NWD(a, b))
