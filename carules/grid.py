# -*- coding: utf-8 -*-
from os import path
from Tkinter import *
from time import sleep

class Grid(object):
	"""Grid class. Handles the painting."""
	# Default title
	title = "CA-Rules!"
	launcher = path.join("rsc", "pulsar-launcher.gif")

	def __init__(self, width, heigh, cell_side, refresh=0.1,
		alive='black', death='white'):
		self.width = width
		self.heigh = heigh
		self.cell_side = cell_side
		self.refresh = refresh
		self.alive = alive
		self.death = death
		self.window = Tk()
		self.window.call('wm', 'iconphoto', self.window,
			PhotoImage(file=Grid.launcher))
		self.window.title(Grid.title)
		self.canvas = Canvas(self.window, width=self.width, height=self.heigh)
		self.canvas.pack()
		self.cell_matrix = []
		for i in range(self.heigh / self.cell_side):
			temp = []
			for j in range(self.width / self.cell_side):
				temp.append(self._create_cell(i, j))
			self.cell_matrix.append(temp)

	def paint(self):
		""" Paints the grid"""
		for x in range(self.cell_side, self.width, self.cell_side):
			self.canvas.create_line(x, 0, x, self.heigh, fill="black")
		for y in range(self.cell_side, self.heigh, self.cell_side):
			self.canvas.create_line(0, y, self.width, y, fill="black")

	def _create_cell(self, x, y):
		""" Creates a cell in the grid"""
		# X: Top-left. (x1,y1) = ((x * CELL_SIDE), (y * CELL_SIDE))
		x1 = x * self.cell_side
		y1 = y * self.cell_side
		# Y: Bottom-right. (x2,y2) = ((x * CELL_SIDE + CELL_SIDE),
		# (y * CELL_SIDE + CELL_SIDE) )
		x2 = x1 + self.cell_side
		y2 = y1 + self.cell_side
		colour = self.death
		return self.canvas.create_rectangle(x1, y1, x2, y2, fill=colour)

	def fill_cell(self, x, y, colour="black"):
		""" Paints the cell at (x, y) in the grid. If no colour is specified,
			the default one is black.
		"""
		#print "Fill cell %r" % (self.cell_matrix[x][y])
		self.canvas.itemconfig(self.cell_matrix[x][y], fill=colour)
		self.window.update_idletasks()

	def delete_cell(self, x, y):
		""" Deletes the cell at (x,y) in the grid."""
		#print "Delete cell cell %r" % (self.cell_matrix[x][y])
		self.canvas.itemconfig(self.cell_matrix[x][y], fill=self.death)
		self.window.update_idletasks()
		
	def set_title(self, title):
		""" Sets the title to the window. Will have 'CA-Rules! - ' plus
			the passed string.
		"""
		self.window.title(Grid.title + " - " + title)

	def get_cell_colour(self, x, y):
		""" Returns the colour of the cell at (x, y)."""
		return self.canvas.itemcget(self.cell_matrix[x][y], "fill")

	def get_num_xcells(self):
		""" Returns the number of x cells."""
		return self.width / self.cell_side

	def get_num_ycells(self):
		""" Returns the number of y cells."""
		return self.heigh / self.cell_side

	def freeze(self):
		""" Freezes the window the specified number of seconds. """
		sleep(self.refresh)

	def get_alive_colour(self):
		""" Returns the colour specified for alive cells."""
		return self.alive

	def get_death_colour(self):
		""" Returns the colour specified for death cells."""
		return self.death
