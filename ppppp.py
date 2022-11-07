
#def mnoz(a,b):
	#return a*b

#wynik = mnoz(int(input()),int(input()))

#print(wynik)
fib=[1,1]
li=0;
fib.append(fib[li] + fib[li+1])

for pętla in range(0,10):
        
        li=li+1
        fib.append(fib[li] + fib[li+1])
print (fib)
