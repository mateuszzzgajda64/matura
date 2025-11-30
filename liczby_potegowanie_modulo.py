def PotegowanieModuloRekurencyjnie(a , b , m):
    if b == 0:
        return 1
    if b % 2 == 0:
        return PotegowanieModuloRekurencyjnie(a*a%m , b // 2, m)
    return (a * PotegowanieModuloRekurencyjnie(a , b - 1, m)) % m


a = int(input())
b = int(input())
m = int(input())
print(PotegowanieModuloRekurencyjnie(a,b,m))
