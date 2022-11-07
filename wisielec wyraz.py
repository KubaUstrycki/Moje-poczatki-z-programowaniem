import random

wyrazy = ['orkiestra','pilnować','pizza','sieć','bohaterka','okno','nagroda','kochać','forum','uniwersytet','liść','zbiór','pasek','wibrować','kierownica','spacer','wnuczek','upośledzenie','czarownik','gen','monstrum','połowa','moda','prowiant','medytować','samolot','historia','błąd','wiersz','sukces','kochanek','bezpieczeństwo','przodek','pień','wakacje','młodzież','słoń','świętować','nieszczęście','reżim','demonstracja','żaba','walka','truskawka','tabletka','łza','prostokąt','most','meczet','gazeta','ulica','album','tendencja','minimum','dowcip','płonąć','podziwiać','boks','powstać','znamię','lekcja','kazanie','głośnik','pamiętnik','ważyć','pilot','patelnia','krawiec','podróż','bawełna','wejście','Sand','krzyk','krytyk','napój','wodospad','szczelina','błogosławieństwo','komplement','muszla','chłopiec','kwiz','scena','diagram','równowaga','zakup','przeszłość','nauka','tłumaczyć','laser','ciemność','siekiera','iluzja','ciasto','węzeł','pudel','zebranie','futbol','zdrowie','królowa']

def wisielec(wyrazOryginal):
    wyraz = wyrazOryginal.lower()
    wybrane = []
    doPokazania = "_ "*len(wyraz) 
    wszystkieOdgadniete = False

    while not wszystkieOdgadniete:
        litera = input(doPokazania + " | podaj literę: ")
        for l in litera.lower():
            wybrane.append(l)

        wszystkieOdgadniete = True
        doPokazania = ""
        for l in wyrazOryginal :
            if wybrane.count(l.lower()) > 0 :
                doPokazania = doPokazania + l + " "
            else :
                doPokazania = doPokazania + "_ "
                wszystkieOdgadniete = False
    print("")
    print("Odgadłeś!")
    print(wyrazOryginal + "!!!!")
    print("")
      


n = random.randint(0, len(wyrazy))
wisielec(wyrazy[n])

