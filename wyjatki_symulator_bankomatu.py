import random

def wpiszPin(proby = 3):
    for i in range(proby):
        proba = input('Wpisz PIN: ')
        if len(proba) == 4:
            return True
        else:
            print('Błędny PIN')
    return False

def menu():
    print("\n---- MENU ----")
    print("1. Sprawdź saldo")
    print("2. Wypłać środki")
    print("3. Wpłać środki")
    print("4. Wyloguj (powrót do ekranu logowania)")
    print("5. Zakończ program")
    print("--------------")

def main():
    saldo = random.randint(1,200000000)
    konsola = True

    while konsola:
        print('Witamy w banku xyz')
        zalogowano = wpiszPin(proby = 3)
        if not zalogowano:
            print("Przekroczono limit prób PIN. Powrót do ekranu startowego.\n")
            continue

        while True:
            menu()
            wybor = int(input('wybierz operacje 1 - 5: '))
            if wybor == 1:
                print('Twoje saldo wynosi ' , saldo , ' PLN')
            elif wybor == 2:
                kwota = int(input('ile PLN chcesz wypłacić? '))
                if kwota <= 0:
                    print('Podaj kwotę większą od 0')
                elif kwota > saldo:
                    print("Niewystarczające środki")
                else:
                    saldo = saldo - kwota
                    print(f'wyplacono {kwota} PLN. Nowe saldo: {saldo}')
            elif wybor == 3:
                kwota = int(input('Ile chcesz wpłacić? '))
                if kwota <= 0:
                    print('Podaj kwotę większą od 0')
                else:
                    saldo = saldo + kwota
                    print(f'wplacono {kwota} PLN. Nowe saldo: {saldo}')
            elif wybor == 4:
                print("Wylogowano. Powrót do ekranu logowania")
                break
            elif wybor == 5:
                print("Zamykanie programu. Do widzenia!")
                konsola = False
                break
            else:
                print("Nieprawidłowy wybór. Wybierz 1 - 5")

if __name__ == "__main__":
    main()
