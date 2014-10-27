# -*- coding: utf-8 -*-
from grid import Grid
from automaton import GameOfLife

def main():
	gof = GameOfLife(Grid(600, 600, 20))
	gof.generate_random(250)
	gof.start()	

if __name__ == '__main__':
	main()