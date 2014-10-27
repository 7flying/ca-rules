# -*- coding: utf-8 -*-
from grid import Grid
from automaton import GameOfLife, DayAndNight, LifeWithoutDeath, HighLife, \
	Seeds, Rule

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
	
	# Life without death
	lwd = LifeWithoutDeath(my_grid)
	lwd.generate_random(150)
	lwd.start()
	
	# High Life
	hl = HighLife(my_grid)
	hl.generate_random(550)
	hl.start()
	
	# Seeds
	seeds = Seeds(my_grid)
	seeds.generate_random(250)
	seeds.start()
	"""
	# General rule
	rule_gol = Rule(my_grid, [3], [2, 3])
	rule_gol.generate_random(250)
	rule_gol.start()


if __name__ == '__main__':
	main()