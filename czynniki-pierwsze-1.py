def jestPodzielna(liczba, dzielnik):
    d = liczba / dzielnik
    if round(d) == d:
        return True
    else:
        return False


def czynnikiPierwsze(li):
    dz = 2
    czynnikiPierwsze = []

    while li > 1:
        if jestPodzielna(li, dz):
            czynnikiPierwsze.append(dz)
            li = round(li / dz)
        else:
            dz = dz + 1
    return czynnikiPierwsze


for x in range (1,1001):
    tab = czynnikiPierwsze (x)
    print (x, tab)

