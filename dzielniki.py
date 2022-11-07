def dzielnikiNapis(liczba) :
	print ("---")
	print ("Dzielniki liczby:", liczba)
	dzielniki(liczba)

def dzielniki(liczba) :
	for x in range(1, liczba + 1):
		d = liczba / x
		if d == round (d) :
			print (x)

def dzielnikiTablica(liczba) :
	dzielniki = []
	for x in range(1, liczba + 1):
		d = liczba / x
		if d == round (d) :
			dzielniki.append(x)
	return dzielniki

d = dzielnikiTablica(1223)
print (d)
