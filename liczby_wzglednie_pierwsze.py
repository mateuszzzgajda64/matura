n = int(input())
m = int(input())

def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

if NWD(n , m) == 1:
    print("Liczby są względnie pierwsze")
else:
    print("Liczby nie są względnie pierwsze")
