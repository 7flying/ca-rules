# -*- coding: utf-8 -*-
from grid import Grid
from automaton import GameOfLife, DayAndNight, LifeWithoutDeath, HighLife

def main():
	
	my_grid = Grid(350, 350, 10)
	"""
	# Game of Life
	gof = GameOfLife(my_grid)
	gof.generate_random(500)
	gof.start()

	# Day & Night
	dan = DayAndNight(my_grid)
	dan.generate_random(500)
	dan.start()
	"""
	# Life without death
	lwd = LifeWithoutDeath(my_grid)
	lwd.generate_random(150)
	lwd.start()
	"""
	# High Life
	hl = HighLife(my_grid)
	hl.generate_random(550)
	hl.start()
	"""

if __name__ == '__main__':
	main()