def jestPodzielna(liczba, dzielnik):
    d = liczba / dzielnik
    if round(d) == d:
        return True
    else:
        return False


def czynnikiPierwsze(li):
    dz = 2
    while li > 1:
        if jestPodzielna(li, dz):
            print(f'{li:10} | {dz:5}')
            li = round(li / dz)
        else:
            dz = dz + 1


def czynnikiPierwsze2(liczba1, liczba2):
    dz = 2
    print ("###")
    while liczba1 > 1 and liczba2 > 1:
        if jestPodzielna(liczba1, dz) and jestPodzielna(liczba2, dz):
            print(f'{liczba1:10} | {liczba2:10} | {dz:5}')
            liczba1 = round(liczba1 / dz)
            liczba2 = round(liczba2 / dz)
        elif jestPodzielna(liczba1, dz):
            liczba1 = round(liczba1 / dz)
        elif jestPodzielna(liczba2, dz):
            liczba2 = round(liczba2 / dz)
        else:
            dz = dz + 1


czynnikiPierwsze2(24, 18)
czynnikiPierwsze2(24, 124)
czynnikiPierwsze2(24, 12)
