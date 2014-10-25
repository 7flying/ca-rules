# -*- coding: utf-8 -*-
from grid import Grid

def main():
	mygrid = Grid(600, 600, 20)
	mygrid.paint()
	mygrid.fill_cell(1, 2)

if __name__ == '__main__':
	main()