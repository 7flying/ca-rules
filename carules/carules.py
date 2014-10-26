# -*- coding: utf-8 -*-
from grid import Grid

def main():
	mygrid = Grid(600, 600, 20)
	mygrid.paint()
	mygrid.fill_cell(1, 3)
	mygrid.delete_cell(1, 3)
	mygrid.fill_cell(4, 4)
	print mygrid.get_cell_colour(4,4)

if __name__ == '__main__':
	main()