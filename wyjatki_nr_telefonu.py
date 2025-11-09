m = str(input())

n = ''

for litera in m:
    if litera != ' ':
        n = n + litera

tabznakow = '+1234567890'
tabcyfr = '1234567890'

czyPoprawny = True

for i in range(len(n)):
    if n[i] not in tabznakow:
        czyPoprawny = False
        break

if czyPoprawny:
    if len(n) == 9:
        for znak in n:
            if znak not in tabcyfr:
                czyPoprawny = False
                break
    elif len(n) == 12 and n[0:3] == '+48':
        for znak in n[3: ]:
            if znak not in tabcyfr:
                czyPoprawny = False
                break
    else:
        czyPoprawny = False

if czyPoprawny:
    print('Poprawny numer telefonu')
else:
    print('Niepoprawny numer telefonu')
