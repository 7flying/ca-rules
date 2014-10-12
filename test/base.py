# -*- coding: utf-8 -*-
from Tkinter import *

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_X = CELL_Y = 10

def paint_grid(canvas):
	for x in range(10, CANVAS_WIDTH, 10):
		canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill="black")
	for y in range(10, CANVAS_HEIGHT, 10):
		canvas.create_line(0, y, CANVAS_WIDTH, y, fill="black")

def ufill_cell(canvas, x, y, fill):
	rect = canvas.create_rectangle(10, 10, 20, 20, fill="blue")
	canvas.delete(rect)

def main():
	tinker = Tk()
	wind = Canvas(tinker, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
	wind.pack()
	paint_grid(wind)
	ufill_cell(wind, 10, 10, "blue")
	mainloop()

if __name__ == '__main__':
	main()
