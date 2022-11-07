def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    if b != 0:
        return a / b


def dodawanie(a, b):
    return a + b

###############################################


for b in range(0, 3):
    for a in range(0, 3):
        print(a, b)
        print("wynik dzielenia    -->", dzielenie(a, b))
        print("wynik mnożenia     -->", mnozenie(a, b))
        print("wynik odejmowania  -->", odejmowanie(a, b))
        print("wynik dodawania    -->", dodawanie(a, b))
