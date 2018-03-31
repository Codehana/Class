#! /usr/bin/env python3
import random

class Kocky:
	def __init__(self, jmeno, life=9):
		self.jmeno = jmeno
		self.life = life
		

	def zamnoukej(self):
		print("Mňau!")
#	def zivot(self):
#		self.life = 9
	def je_ziva(self):
		if self.life == 0:
			print("Jsem mrtvá.")
		else:
			print("Jsem živá.")
	def uber_zivot(self):
		self.life = self.life -1
	def snez(self):
		jidlo = ["ryba","granule","mléko"]
		a = random.choice(jidlo)
		if a == "ryba":
			if self.life != 0 and self.life != 9:
				self.life = self.life + 1
Micka = Kocky("Micka")

Micka.zamnoukej()
Micka.je_ziva()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.uber_zivot()
Micka.snez()
Micka.snez()
print(Micka.life)
