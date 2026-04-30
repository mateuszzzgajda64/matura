s = str(input())
k = str(input())


def szyfruj(s , k):
    n = len(s)
    m = len(k)
    d = 0
    w = ''
    for i in range(n):
        d = d % m
        l = s[i]
        l = ord(l) - 65
        klucz = k[d]
        klucz = ord(klucz) - 65
        r = (l - klucz) % 26
        l = chr(r + 65)
        w = w + l
        d = d + 1
    return w

w = szyfruj(s, k)
print(w)
