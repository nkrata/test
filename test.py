while True :
    ##Menu z różnymi zadaniami
    print("aby zobaczyć informacje o autorze, wciśnij \"1\"")
    print("aby zobaczyć wykonane dziś zadanie o czarodzieju, wściśnij \"2\"")
    print("aby zobaczyć wykonane dziś zadanie o generatorze haseł, wściśnij \"3\"")
    print("aby zobaczyć wykonane dziś zadanie o menu, wściśnij \"4\"")
    print("aby zobaczyć wykonane dziś zadanie o grze z komputerem, wściśnij \"5\"")
    print("aby zakończyć program wściśnij \"6\"")
    znak = input()
    if znak == "1":
        ##wyświetla informacje o autorze
        print("Natalia Krata")
    elif znak == "2":
        #wyświetla słowo w zależności od wylosowanej liczby
        import random
        wylosowana=random.random()
        if wylosowana<=0.001:
            print("sztabka złota")
        if wylosowana >0.001 and wylosowana <=0.02:
            print("konsola")
        if wylosowana >0.02 and wylosowana <=0.1:
            print("husteczka")
        if wylosowana >0.1 and wylosowana <=0.5:
            print("mikser")
        if wylosowana >0.5 and wylosowana <=0.99:
            print("balonik")
    elif znak == "4":
        #treść tego zadania jest całym kodem test.py
        print("właśnie widzisz to zadanie")
    elif znak == "3":
        #tworzy losowe hasło
        import random
        baza_litery="abcdefghijklmnoprstuwqxz"
        baza_cyfry="0123456789"
        print(random.choice(baza_litery),random.choice(baza_litery),random.choice(baza_litery),random.choice(baza_litery) + random.choice(baza_cyfry),random.choice(baza_cyfry),random.choice(baza_cyfry))
    elif znak == "5":
        #kto poda większą liczbę użytkownik czy komputer. Wyświetla się 10 prób. 
        import random
        punkty_gracza=0
        punkty_komputera=0
        for i in range(1,11):
            liczba_komputera = random.randint(0,100)
            print("Podaj liczbę od 0 do 100")
            liczba_gracza = int(input())
            print(liczba_komputera)
            if liczba_gracza > liczba_komputera:
                print("wygrałeś - dostajesz 1 punkt")
                punkty_gracza+=1
            elif liczba_komputera > liczba_gracza:
                print("przegrałeś - komputer dostaje 1 punkt")
                punkty_komputera+=1
            else:
                print("Remis - 0 punktów")
        print("zdobyłeś",punkty_gracza,"punktów", "a ja", punkty_komputera, "punktów")
    elif znak == "6":
        break
    else:
        print("nieprawidłowy znak")
