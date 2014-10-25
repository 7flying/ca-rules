# -*- coding: utf-8 -*-
from Tkinter import *

class Grid(object):
	"""Grid class. Handles the painting."""
	# Default title
	title = "CA-Rules!"

	def __init__(self, width, heigh, cell_side):
		self.width = width
		self.heigh = heigh
		self.cell_side = cell_side
		self.cell_matrix = []
		for i in range(self.heigh / self.cell_side):
			temp = []
			for j in range(self.width / self.cell_side):
				temp.append(None)
			self.cell_matrix.append(temp)

	def paint(self):
		""" Paints the grid"""
		self.window = Tk()
		self.window.title(Grid.title)
		self.canvas = Canvas(self.window, width=self.width, height=self.heigh)
		self.canvas.pack()
		for x in range(self.cell_side, self.width, self.cell_side):
			self.canvas.create_line(x, 0, x, self.heigh, fill="black")
		for y in range(self.cell_side, self.heigh, self.cell_side):
			self.canvas.create_line(0, y, self.width, y, fill="black")
		self.window.mainloop()

	def fill_cell(self, x, y):
		""" Paints the cell at (x, y) in the grid."""
		# X: Top-left. (x1,y1) = ((x * CELL_SIDE), (y * CELL_SIDE))
		x1 = x * self.cell_side
		y1 = y * self.cell_side
		# Y: Bottom-right. (x2,y2) = ((x * CELL_SIDE + CELL_SIDE),
		# (y * CELL_SIDE + CELL_SIDE) )
		x2 = x1 + self.cell_side
		y2 = y1 + self.cell_side
		temp_rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
		#self.cell_matrix[x][y] = temp_rect
		self.window.update()

	def delete_cell(self, x, y):
		""" Deletes the cell at (x,y) in the grid."""
		self.canvas.delete(self.cell_matrix[x][y])
		self.cell_matrix[x][y] = None
