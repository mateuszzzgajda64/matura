ciag = input()
a = int(input())

def dziel(napis , x):
    tab = napis.split(' ')
    linia = ''
    for i in tab:
        if len(linia) + len(i) + 1 <= x:
            if linia:
                linia += ' '
            linia += i
        else:
            print(linia)
            linia = i
    if linia:
        print(linia)

dziel(ciag, a)

