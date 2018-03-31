#! /usr/bin/env python3


class Telesa:
	def obsah():
		raise NotImplementedError()
	def obvod():
		raise NotImplementedError()

class Trojuhelnik(Telesa):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		
	def obvod(self):
		return self.a + self.b + self.c
	def obsah(self):
		s = self.obvod()/2
		return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5


class Ctverec(Telesa):
	def __init__(self, strana):
		self.strana = strana
	def obsah(self):
		return float(self.strana * self.strana)
	def obvod(self):
		return float(self.strana * 4)


class Obdelnik(Telesa):
	def __init__(self, strana_1, strana_2):
		self.strana_1 = strana_1
		self.strana_2 = strana_2
	def obsah(self):
		return float(self.strana_1 * self.strana_2)
	def obvod(self):
		return (self.strana_1 + self.strana_2) * 2.0


t = [Trojuhelnik(3,4,5), Ctverec(4), Obdelnik(4,5)]

for teleso in t:
	obsah = teleso.obsah()
	print("Obsah je",obsah)
	#obvod = 
