# -*- coding: utf-8 -*-
from neighborhood import Moore
from grid import Grid

class Rule(object):
	""" To implement general rules."""

	def __init__(self, grid, born="", survive=""):
		self.grid = grid
		self.cells = []
		for i in range(self.grid.get_num_ycells()):
			temp = []
			for j in range(self.grid.get_num_xcells()):
				temp.append("white")
			self.cells.append(temp)
		self.neigh = Moore(self.grid)
		self.born = [str(i) for i in born]
		self.survive =  [str(i) for i in survive]
		self.grid.set_title("B" + "".join(self.born) + " / S" \
			 + "".join(self.survive))

	def paint(self):
		""" Paints the automaton defined by the rule."""
		ret = False
		for y in range(self.grid.get_num_ycells()):
			for x in range(self.grid.get_num_xcells()):
				self.grid.fill_cell(x, y, self.cells[x][y])
				if self.cells[x][y] == "black":
					ret = True
		return ret

	def start(self):
		""" Starts the automaton defined by the rule."""
		some_cell_alive = True
		while some_cell_alive:
			#self.grid.freeze()
			some_cell_alive = self.paint()
			self.next_generation()

	def next_generation(self):
		for i in range(self.grid.get_num_ycells()):
			for j in range(self.grid.get_num_xcells()):
				count = self.neigh.count_neighbors(j, i)
				# Survive
				if self.grid.get_cell_colour(j, i) == "black":
					if str(count) not in self.survive:
						self.cells[j][i] = "white"
				# Born
				elif str(count) in self.born:
					self.cells[j][i] = "black"

	def get_cell_matrix(self):
		return self.cells
