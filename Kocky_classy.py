#! /usr/bin/env python3
import random

class Kocka:
	def __init__(self , jmeno, srst="seda"):
		self.srst = srst
		self.jmeno = jmeno

	def zmen_srst(self):
		barvy = ["bila","modra","cerna","ruzova","zluta","zelena","hneda","fialova","flek","cervena"]
		self.srst = barvy[1]
	def dej_jmeno(self):
		seznam_jmen = ["Mourek","Micka","Mikes"]
		self.jmeno = seznam_jmen[2]

kocicky = [Kocka("Mourek"), Kocka("Micka"), Kocka("Mikes")]

kocicky[1].zmen_srst()
kocicky[1].dej_jmeno()
print(kocicky[1].srst)
print(kocicky[1].jmeno)
