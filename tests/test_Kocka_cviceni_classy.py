#! /usr/bin/env python3

import pytest
from Kocka_cviceni_classy import Kocky , MrtvaKockaError


def test_Kocky():
	Micka = Kocky("Micka")
	assert Micka.zamnoukej() == "Mnau!"

def test_Uber():
	Micka = Kocky("Micka")
	Micka.uber_zivot()
	assert Micka.life == 8

def test_Zabita_Kocka():
	Micka = Kocky("Micka",life=1)
	with pytest.raises(MrtvaKockaError):
		Micka.uber_zivot()
	
	





