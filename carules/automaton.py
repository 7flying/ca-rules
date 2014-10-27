# -*- coding: utf-8 -*-
import abc
import random

from grid import Grid
from neighborhood import Moore

class CellularAutomaton(object):

	def __init__(self, grid):
		self.grid = grid
		self.cells = []
		for i in range(self.grid.get_num_ycells()):
			temp = []
			for j in range(self.grid.get_num_xcells()):
				temp.append("white")
			self.cells.append(temp)

	@abc.abstractmethod
	def next_generation(self):
		""" Generates the next generation."""

	def paint(self):
		""" Paints the automaton."""
		ret = False
		for y in range(self.grid.get_num_ycells()):
			for x in range(self.grid.get_num_xcells()):
				self.grid.fill_cell(x, y, self.cells[x][y])
				if self.cells[x][y] == "black":
					ret = True
		return ret

	def start(self):
		""" Starts the automaton."""
		some_cell_alive = True
		while some_cell_alive:
			#self.grid.freeze()
			some_cell_alive = self.paint()
			self.next_generation()

	def generate_random(self, num):
		""" Generates some random cells."""
		for x in range(num):
			self.cells[random.randint(
				0, self.grid.get_num_xcells() - 1)][random.randint(
				0, self.grid.get_num_ycells() - 1 )] = "black"
		

class GameOfLife(CellularAutomaton):
	""" Conway's Game of Life cellular automaton implementation."""
	title = "Game of Life"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(GameOfLife.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For GoL (B3/S23)
			Cell dies: 	- four or more neighbors (overpopulation).
						- one or none neighbor (isolation).
  			Cell survives: two or three neighbors.
  			Birth: 3 neighbors.
  		"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i)
				# Survive
				if self.grid.get_cell_colour(j, i) == "black":
					if count < 2 or count > 3:
						self.cells[j][i] = "white"
					elif count == 2 or count == 3:
						self.cells[j][i] = "black"	
				# Born
				elif count ==3:
					self.cells[j][i] = "black"


class DayAndNight(CellularAutomaton):
	""" Day & Night cellular automaton implementation."""
	title = "Day & Night"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(DayAndNight.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For Day & Night (B3678/S34678)"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i)
				# Survive
				if self.grid.get_cell_colour(j, i) == "black":
					if (count > 5) or (count > 2 and count < 5):
						self.cells[j][i] = "black"
					else:
						self.cells[j][i] = "white"
				# Born
				elif count == 3 or count > 5: 
					self.cells[j][i] = "black"


class LifeWithoutDeath(CellularAutomaton):
	""" Life Without Death cellular automaton implementation."""
	title = "Life Without Death"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(LifeWithoutDeath.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For LwoD : S01245678/B3"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i)
				# Survive
				if self.grid.get_cell_colour(j, i) == "black":
					self.cells[j][i] = "black"
				# Born
				elif count == 3:
					 self.cells[j][i] = "black"

class HighLife(CellularAutomaton):
	""" HighLife cellular automaton implementation"""
	title = "High Life"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(HighLife.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For HighLife (B3678/S34678)"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i)
				# Survive
				if self.grid.get_cell_colour(j, i) == "black":
					if count == 2 or count == 3:
						self.cells[j][i] = "black"
					else:
						self.cells[j][i] = "white"
				# Born
				elif count == 3 or count == 6:
					self.cells[j][i] = "black"
