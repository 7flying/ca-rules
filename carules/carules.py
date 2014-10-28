# -*- coding: utf-8 -*-
from sys import argv, exit
import getopt
from grid import Grid
from automaton import CellularAutomaton

def usage():
	print "\n  carules - generate a cellular automaton"
	print "    carules.py [OPTIONS]..."
	print "\n  OPTIONS"
	print "\n  -n AUTOMATON, --name=AUTOMATON"
	print "\t    Generates the automaton given its name.\n" +\
		  "\t    Use '--list' option to known which ones are implemented."
	print "\n  -r, --rule=RULE"
	print "\t    Being RULE: <born_rule>:<survive_rule>, generates the automaton\n" + \
		  "\t    described by the rule.\n\t    Example: -r 3:23" 
	print "\n  -c CELLSIDE, -cell=CELLSIDE"
	print "\t    Defines the cell side in the grid (cells are square).\n" + \
		  "\t    By default 10."
	print "\n  -g GRIDSIDE, -grid=GRIDSIDE"
	print "\t    Defines the side of the grid window (the window is square).\n" + \
		  "\t    By default the window is 350x350."
	print "\n  -l, --list"
	print "\t    Shows a list of the implemented automata.\n" + \
		  "\t    Use these names along with '--name' option to generate automata."
	print "\n  -h --help"
	print "\t    Shows what you are currently reading."

def plist():
	""" Prints the list of implemented Cellular Automata """
	for auto in CellularAutomaton.__subclasses__():
		print "\t-" + auto.__name__

def main(argv):
	try:
		options, args = getopt.getopt(argv, "r:n:c:g:lh", [
						'rule=', 'name=', 'list', 'help'])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	else:
		def_grid = 350
		def_cell = 10
		for opt, arg in sorted(options):
			if opt in ('-h', '--help'):
				usage()
				exit(2)
			elif opt in ('-l', '--list'):
				plist()
			elif opt in ('-c', '--cell'):
				if int(arg) > 0:
					def_cell = int(arg)
				else:
					print "Sure, cells of 0x0."
					exit(2)
			elif opt in ('-g', '--grid'):
				if int(arg) > 0:
					def_grid = int(arg)
				else:
					print "Good luck with a grid of 0x0."
					exit(2)
			elif opt in ('-r', '--rule'):
				rule = arg

			elif opt in ('-n', '--name'):
				name = arg
				thegrid = Grid(def_grid, def_grid, def_cell)
				aut = CellularAutomaton.factory(name, thegrid)
				CellularAutomaton.generate_random(250, thegrid,
					aut.get_cell_matrix())
				aut.start()
			else:
				usage()
				exit(2)

if __name__ == '__main__':
	main(argv[1:])