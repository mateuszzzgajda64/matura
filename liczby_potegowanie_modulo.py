def PotegowanieModuloRekurencyjnie(a , b , m):
    if b == 0:
        return 1
    if b % 2 == 0:
        return PotegowanieModuloRekurencyjnie(a*a%m , b // 2, m)
    return (a * PotegowanieModuloRekurencyjnie(a , b - 1, m)) % m

def PotegowanieModuloIteracyjnie(a , b , m):
    w = 1
    while b >0:
        if b % 2 == 1:
            w = (w*a)% m
        a = (a*a)%m
        b = b //2
    return w

a = int(input())
b = int(input())
m = int(input())
print(PotegowanieModuloRekurencyjnie(a,b,m))
