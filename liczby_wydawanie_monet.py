nominaly = [20 , 10 , 50 , 1 , 2 , 5]
reszta = int(input())

def sortowanie(nominaly):
    for i in range (len(nominaly) - 1):
        for j in range (len(nominaly) - i -  1):
            if nominaly[j] < nominaly[j + 1]:
                nominaly[j], nominaly[j + 1] = nominaly[j + 1], nominaly[j]
    return nominaly
nominaly = sortowanie(nominaly)

def wydawanie(r , nominaly):
    wydane = []
    for i in range (len(nominaly)):
        while r >= nominaly[i]:
            wydane.append(nominaly[i])
            r -= nominaly[i]
    return wydane

print(wydawanie(reszta, nominaly))
print(sortowanie(nominaly))
