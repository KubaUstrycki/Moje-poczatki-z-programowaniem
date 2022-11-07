import random

PAPIER = "Papier"
KAMIEN = "Kamień"
NOZYCE = "Nożyce"

pu = "p"
ku = "k"
nu = "n"

re = [PAPIER, KAMIEN, NOZYCE]


def graj():
    print("gramy w Papier, Kamień, Nożyce")
    wygraneUzytkownika = 0
    wygraneKomputera = 0

    while wygraneKomputera < 3 and wygraneUzytkownika < 3:
        print("_"*54)
        l = input("wybierz ( p = papier) , ( k = kamień ) ( n = nożyce)|:")
        r = random.choice(re)
        print("Komputer wybrał: ", r)

        if l == pu:
            if r == PAPIER:
                print("\|REMIS|/")
            if r == KAMIEN:
                print("<Użytkownik wygrywa>")
                wygraneUzytkownika += 1
            if r == NOZYCE:
                print("[Komputer wygrywa]")
                wygraneKomputera += 1
        elif l == ku:
            if r == PAPIER:
                print("[Komputer wygrywa]")
                wygraneKomputera += 1
            if r == KAMIEN:
                print("\|REMIS|/")
            if r == NOZYCE:
                print("<Użytkownik wygrywa>")
                wygraneUzytkownika += 1
        elif l == nu:
            if r == PAPIER:
                print("<Użytkownik wygrywa>")
                wygraneUzytkownika += 1
            if r == KAMIEN:
                print("[Komputer wygrywa]")
                wygraneKomputera += 1
            if r == NOZYCE:
                print("\|REMIS|/")
        else:
            print("wpisz coś normalnego")

        print("wyniki")
        print("komputer: ", wygraneKomputera,
              "użytkownik: ", wygraneUzytkownika)


graj()
