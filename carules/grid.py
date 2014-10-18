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
		pass

	def unfill_cell(self, x, y):
		pass
