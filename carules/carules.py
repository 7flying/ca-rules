# -*- coding: utf-8 -*-
from grid import Grid
from neighborhood import Moore

def main():
	mygrid = Grid(600, 600, 20)
	mygrid.paint()
	moore = Moore(mygrid)
	mygrid.fill_cell(1, 0)
	mygrid.fill_cell(1, 1)
	mygrid.fill_cell(2, 0)
	mygrid.fill_cell(4, 1)
	mygrid.fill_cell(4, 3)
	mygrid.fill_cell(5, 0)
	print "1,0 =", moore.count_neighbors(1,0)
	print "1,1 =", moore.count_neighbors(1,1)
	print "2,0 =", moore.count_neighbors(2,0)
	print "4,1 =", moore.count_neighbors(4,1)
	print "4,3 =", moore.count_neighbors(4,3)
	print "5,0 =", moore.count_neighbors(5,0)
	print mygrid.get_cell_colour(4,4)

if __name__ == '__main__':
	main()