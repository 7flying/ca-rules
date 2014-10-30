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
				temp.append(grid.get_death_colour())
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
				if self.cells[x][y] == self.grid.get_alive_colour():
					ret = True
		return ret

	def start(self):
		""" Starts the automaton."""
		some_cell_alive = True
		while some_cell_alive:
			#self.grid.freeze()
			some_cell_alive = self.paint()
			self.next_generation()

	@staticmethod
	def generate_random(num, grid, cell_matrix, alive_colour="black"):
		""" Generates some random cells."""
		for x in range(num):
			cell_matrix[random.randint(
				0, grid.get_num_xcells() - 1)][random.randint(
				0, grid.get_num_ycells() - 1 )] = alive_colour

	def get_cell_matrix(self):
		return self.cells

	@staticmethod
	def factory(name, grid):
		if name == "GameOfLife": return GameOfLife(grid)
		if name == "DayAndNight": return DayAndNight(grid)
		if name == "LifeWithoutDeath": return LifeWithoutDeath(grid)
		if name == "HighLife": return HighLife(grid)
		if name == "Seeds": return Seeds(grid)
		

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
				count = self.neigh.count_neighbors(j, i, self.grid.get_alive_colour())
				# Survive
				if self.grid.get_cell_colour(j, i) == self.grid.get_alive_colour():
					if count < 2 or count > 3:
						self.cells[j][i] = self.grid.get_death_colour()
					elif count == 2 or count == 3:
						self.cells[j][i] = self.grid.get_alive_colour()
				# Born
				elif count ==3:
					self.cells[j][i] = self.grid.get_alive_colour()


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
				count = self.neigh.count_neighbors(j, i, self.grid.get_alive_colour())
				# Survive
				if self.grid.get_cell_colour(j, i) == self.grid.get_alive_colour():
					if (count > 5) or (count > 2 and count < 5):
						self.cells[j][i] = self.grid.get_alive_colour()
					else:
						self.cells[j][i] = self.grid.get_death_colour()
				# Born
				elif count == 3 or count > 5: 
					self.cells[j][i] = self.grid.get_alive_colour()


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
				count = self.neigh.count_neighbors(j, i, self.grid.get_alive_colour())
				# Survive
				if self.grid.get_cell_colour(j, i) == self.grid.get_alive_colour():
					self.cells[j][i] = self.grid.get_alive_colour()
				# Born
				elif count == 3:
					 self.cells[j][i] = self.grid.get_alive_colour()


class HighLife(CellularAutomaton):
	""" HighLife cellular automaton implementation."""
	title = "High Life"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(HighLife.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For HighLife (B3678/S34678)"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i, self.grid.get_alive_colour())
				# Survive
				if self.grid.get_cell_colour(j, i) == self.grid.get_alive_colour():
					if count == 2 or count == 3:
						self.cells[j][i] = self.grid.get_alive_colour()
					else:
						self.cells[j][i] = self.grid.get_death_colour()
				# Born
				elif count == 3 or count == 6:
					self.cells[j][i] = self.grid.get_alive_colour()


class Seeds(CellularAutomaton):
	""" Seeds cellular automaton implementation."""
	title = "Seeds"

	def __init__(self, grid):
		CellularAutomaton.__init__(self, grid)
		self.grid.set_title(Seeds.title)
		self.neigh = Moore(self.grid)

	def next_generation(self):
		""" For Seeds (B2/S)"""
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i, self.grid.get_alive_colour())
				# Survive
				if self.grid.get_cell_colour(j, i) == self.grid.get_alive_colour():
					self.cells[j][i] = self.grid.get_death_colour()
				# Born
				elif count == 2:
					self.cells[j][1] = self.grid.get_alive_colour()
