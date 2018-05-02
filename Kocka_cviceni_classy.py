#! /usr/bin/env python3
import random

class MrtvaKockaError(ValueError):
	pass

class Kocky:
	def __init__(self, jmeno, life=9):
		self.jmeno = jmeno
		self.life = life
		

	def zamnoukej(self):
		return "Mnau!"
#	def zivot(self):
#		self.life = 9
	def je_ziva(self):
		if self.life == 0:
			return "Jsem mrtva."
		else:
			return "Jsem ziva."
	def uber_zivot(self):
		self.life = self.life -1
		if self.life == 0:
			raise MrtvaKockaError("Ty vrahu!")
	def snez(self):
		jidlo = ["ryba","granule","mleko"]
		a = random.choice(jidlo)
		if a == "ryba":
			if self.life != 0 and self.life != 9:
				self.life = self.life + 1
