# -*- coding: utf-8 -*-
import abc

class Neighborhood(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def count_neighbors(self, colour):
		""" Returns the count of neighbors."""

class Moore(Neighborhood):
	""" Class implementing the Moore neighborhood."""
	def __init__(self, grid):
		self.grid = grid

	def count_neighbors(self, colour="black"):
		pass

class VonNeumann(Neighborhood):
	""" Class implementing the von Neumann neighborhood."""
	def __init__(self, grid, manhattan=1):
		""" By default the von Neumann neighborhood of a cell is the set of
			cells at a Manhattan distance of 1.
		"""
		self.grid = grid
		self.manhattan = manhattan

	def count_neighbors(self, colour="black"):
		pass
