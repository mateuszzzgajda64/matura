def szybkiepotegowanierekurencyje(a , b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return szybkiepotegowanierekurencyje(a * a , b // 2)
    else:
        return a * szybkiepotegowanierekurencyje(a , b - 1)

a = int(input())
b = int(input())
print(szybkiepotegowanierekurencyje(a,b))
