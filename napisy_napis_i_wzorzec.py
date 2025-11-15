napis = str(input())
wzorzec = str(input())

def wypisz(slowo , w):
    for i in range(len(slowo) - len(w) + 1):
        if slowo[i:i+len(w)] == w:
            print(i)

wypisz(napis, wzorzec)
