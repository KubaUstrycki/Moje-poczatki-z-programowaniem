def wyswietLiczbe() :
    l = input("podaj liczbę: ")
    try:
        liczba = int(l)
        print ("twoja liczba:", liczba)
        return 1
    except ValueError:
        print ("Zła liczba")
        return 0

def wyswietLiczby(ile) :
    for target_list in range(ile):
        if wyswietLiczbe() == 0 :
            exit(1)

print("Cześć!")
wyswietLiczby(4335)

