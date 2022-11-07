import random


def wisielec(liczba):
    l = int(input("zgadnij liczbę: "))
    while l != liczba:
        if l > liczba:
            print("za duża liczba")
        elif l < liczba:
            print("za mala liczba")
        l = int(input("zgadnij liczbę: "))
    print("ZGADłEŚ!!")


wisielec(random.randint(1, 150))
