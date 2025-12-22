print(list("ABC"))

lista = [1 , 2 , 3 , 4 , 5]
lista.extend([6 , 7 , 8])
print(lista)
lista.insert(1 , 6)
print(lista)
lista.remove(4)
print(lista)
lista.pop(5)
print(lista)

tab = ['Ala' , 'ma' , 'kota']
print('*'.join(tab))

arr = [True , True , True]
print(all(arr))
print(any(arr))

arr2 = [4 , 5 , 0 , 3 , 1]
arr2.sort()
print(arr2)

arr3 = [1 ,2 , 3]
arr4 = ['a' , 'b' , 'c']
print(list(zip(arr3, arr4))) # laczy w krotki

osoba1 = {'imie': 'Mateusz' , 'nazwisko': 'Gajda' , 'wiek': 19}
osoba2 = {'imie': 'Mateusz' , 'nazwisko': 'Kowalski' , 'wiek': 20}
osoba1.update(osoba2)
print(osoba1)
print(osoba2['imie'])

import statistics

arr5 = [1 , 2 , 3 , 4 , 4 , 5]
print(statistics.mean(arr5))
print(statistics.median(arr5))
print(statistics.median_low(arr5))
print(statistics.mode(arr5))
print(statistics.variance(arr5))

