#! /usr/bin/env python3

import random

class Genesis:
	def __init__(self, nohy = 4, kozich = None, jidlo = None):
		self.nohy = nohy
		self.kozich = kozich
		self.jidlo = jidlo

	def dej_nohy(self):
		koncetiny = [2,3,4,6]
		self.nohy = random.choice(koncetiny)
		return self.nohy
	def dej_kozich(self):
		kozisek = [True,False]
		self.kozich = random.choice(kozisek)
		return self.kozich
	def dej_jidlo(self):
		papani = ["maso","vegie","oboje"]
		self.jidlo = random.choice(papani)

def udelej_zvirata():
	z = int(input("Kolik má být zvířat? "))
	zvirata = []
	x = Genesis()
	for z in range(z):
		zvirata.append({"nohy": x.dej_nohy(), "kozich": x.dej_kozich(), "jidlo": x.dej_jidlo()})
	return zvirata

print(udelej_zvirata())
