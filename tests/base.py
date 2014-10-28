# -*- coding: utf-8 -*-
from Tkinter import *

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_X = CELL_Y = 35

def paint_grid(canvas):
	for x in range(CELL_X, CANVAS_WIDTH, CELL_Y):
		canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill="black")
	for y in range(CELL_X, CANVAS_HEIGHT, CELL_Y):
		canvas.create_line(0, y, CANVAS_WIDTH, y, fill="black")

def ufill_cell(canvas, x, y, fill):
	rect = canvas.create_rectangle(10, 10, 20, 20, fill="blue")
	canvas.delete(rect)

def main():
	tinker = Tk()
	wind = Canvas(tinker, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
	wind.pack()
	paint_grid(wind)
	
	mainloop()
	ufill_cell(wind, 10, 10, "blue")

if __name__ == '__main__':
	main()
