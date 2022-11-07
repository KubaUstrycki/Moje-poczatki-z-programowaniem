limit = int(input("podaj liczbę: "))
for x in range(1,limit + 1):
    for a in range (1,limit + 1):
        print(x, " * ", a, " =", x*a)