# -*- coding: utf-8 -*-
from grid import Grid
from automaton import GameOfLife, DayAndNight, LifeWithoutDeath

def main():
	"""
	# Game of Life
	gof = GameOfLife(Grid(600, 600, 20))
	gof.generate_random(250)
	gof.start()
	
	# Day & Night
	dan = DayAndNight(Grid(600, 600, 20))
	dan.generate_random(150)
	dan.start()
	"""
	# Life without death
	lwd = LifeWithoutDeath(Grid(600,600, 20))
	lwd.generate_random(2)
	lwd.start()

if __name__ == '__main__':
	main()