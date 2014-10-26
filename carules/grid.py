# -*- coding: utf-8 -*-
from Tkinter import *
from time import sleep

class Grid(object):
	"""Grid class. Handles the painting."""
	# Default title
	title = "CA-Rules!"

	def __init__(self, width, heigh, cell_side):
		self.width = width
		self.heigh = heigh
		self.cell_side = cell_side
		self.window = Tk()
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
		return self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

	def fill_cell(self, x, y):
		""" Paints the cell at (x, y) in the grid."""
		print "Fill cell %r" % (self.cell_matrix[x][y])
		sleep(1)
		self.canvas.itemconfig(self.cell_matrix[x][y], fill="black")
		self.window.update_idletasks()

	def delete_cell(self, x, y):
		""" Deletes the cell at (x,y) in the grid."""
		print "Delete cell cell %r" % (self.cell_matrix[x][y])
		sleep(1)
		self.canvas.itemconfig(self.cell_matrix[x][y], fill="white")
		
		
