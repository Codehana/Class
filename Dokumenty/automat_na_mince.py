#!/usr/bin/python3


x = int(input("Co chcete rozměnit? "))

def aut2(x):
	drobne_mince = [50,20,10,5,2,1]
	pocet_minci = [0,0,0,0,0,0]
	i = 0	
	
	for i in range(6):
		if x//drobne_mince[i] >= 1:
			pocet_minci[i] = x//drobne_mince[i]
			x = x - pocet_minci[i]*drobne_mince[i]
		else:
			pocet_minci[i] = 0
		
	return(pocet_minci)



def automat(x):
	# pocitadla kusu jednotlivych typu minci
	padesat = 0
	dvacet = 0
	deset = 0
	pet = 0
	dve = 0
	jedna = 0
	
	while x != 0:
		if x//50 >= 1:
			padesat = x//50
			x = x - padesat*50
		elif x//20 >= 1:
			dvacet = x//20
			x = x - dvacet*20
		elif x//10 >= 1:
			deset = x//10
			x = x - deset*10
		elif x//5 >= 1:
			pet = x//5
			x = x - pet*5
		elif x//2 >= 1:
			dve = x//2
			x = x - dve*2
		else:
			jedna = x
			x = 0

	return(padesat,dvacet,deset,pet,dve,jedna)

test = aut2(x)

print("50: %d, 20: %d, 10: %d, 5: %d, 2: %d, 1: %d" % (test[0], test[1], test[2], test[3], test[4], test[5]))
