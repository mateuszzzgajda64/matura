n = int(input())
tab = []
for i in range(n):
    tab.append(str(input()))

wzor = str(input())
def sortowaniePrzezWstawianie(slowo):
    arr = list(slowo)
    for i in range(1 , len(arr)):
        k = arr[i]
        j = i-1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = k

    w = ''
    for i in arr:
        w += i
    return w

tab2 = []
for i in range(n):
    tab2.append(sortowaniePrzezWstawianie(tab[i]))

for i in tab2:
    if wzor in i:
        print(i)

