def mniejsza(l1, l2) :
	if l1 > l2 :
		return l2
	return l1
#
#def nazwaFunkcji(argument, parametr, cos) :
#	return argument * parametr * cos


def kwadrtmniejsza(l1,l2) :
	if l1<l2 :
		return l1*l1
	return l2*l2

def kwadrtmniejsza2(l1,l2) :
	m = mniejsza(l1, l2)
	return m*m

k = kwadrtmniejsza(50,49)
print(k)

d = kwadrtmniejsza2(50,49)
print(d)