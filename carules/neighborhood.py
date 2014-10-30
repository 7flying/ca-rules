# -*- coding: utf-8 -*-
import abc

class Neighborhood(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def count_neighbors(self, x, y, colour):
		""" Returns the count of neighbors of a cell at (x,y)."""

class Moore(Neighborhood):
	""" Class implementing the Moore neighborhood."""
	def __init__(self, grid):
		self.grid = grid

	def count_neighbors(self, x, y, colour="black"):
		""" Counts the neighborhoods of the cell at (x, y) of the given colour.
		 	If no colour is given, it will count black neighbors.
		"""
		# Plan
		# |1|2|3|
		# |4| |5|
 		# |6|7|8|
		count = 0
		# Check safety
		xminus = xplus = yminus = yplus = False
		if y - 1 >= 0:
			yminus = True
		if x - 1 >= 0:
			xminus = True
		if x + 1 < self.grid.get_num_xcells():
			xplus = True
		if y + 1 < self.grid.get_num_ycells():
			yplus = True
		# Count
		if xminus:
			if self.grid.get_cell_colour(x -1, y) == colour:
				count += 1
			if yminus:
				if self.grid.get_cell_colour(x - 1, y -1) == colour:
					count += 1
			if yplus:
				if self.grid.get_cell_colour(x - 1, y +1) == colour:
					count += 1
		if yminus:
			if self.grid.get_cell_colour(x, y - 1) == colour:
				count += 1
			if xplus:
				if self.grid.get_cell_colour(x + 1 , y - 1) == colour:
					count += 1
		if xplus:
			if self.grid.get_cell_colour(x + 1 , y) == colour:
				count += 1
			if yplus:
				if self.grid.get_cell_colour(x + 1, y + 1) == colour:
					count += 1
		if yplus:
			if self.grid.get_cell_colour(x, y + 1) == colour:
				count += 1
		return count


class VonNeumann(Neighborhood):
	""" Class implementing the von Neumann neighborhood."""
	def __init__(self, grid, manhattan=1):
		""" By default the von Neumann neighborhood of a cell is the set of
			cells at a Manhattan distance of 1.
		"""
		self.grid = grid
		self.manhattan = manhattan

	def count_neighbors(self, x, y, colour="black"):
		pass
