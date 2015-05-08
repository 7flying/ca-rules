CA-Rules!
=========

CA-Rules is a cellular automata command-line generation tool.

<a href="url"><img src="https://github.com/7flying/ca-rules/blob/master/gallery/maze.gif" height="300" width="300" ></a>

How to use
----------

#### Automata Generation

* You can generate an automaton giving its name.

  Game of Life is generated this way:

  ```
  python carules.py --name GameOfLife
  ```
  To get the list of known automata names use the *--list* option.
  ```
  python carules.py --list
  ```

* If the automata is not implemented just type its rule.

  Rules are defined in the "B/C" where B is the number of neighbors needed for a cell to be born and C is the number of neighbors needed for a cell to survive.

  Game of Life has a B3/S23 rule, so type:
  ```
  python carules.py --rule 3:23
  ```
  and GoL will appear.
  
  Rules are defined in the following style: bornRule:surviveRule.

#### Other options

* The window size can be changed using *--grid SIZE* option.
  
  To run High Life in a 300x300 window:
  ```
  python carules.py --grid 300 -n HighLife
  ```
* Cell side can be changed using *--cell SIZE* option.
  
  Generate Amoeba B357/S1358 rule with cells of 15x15:
  ```
  python carules.py --cell 15 -r 357:1358
  ```
* Change colours!
  Use *--fill ALIVE:DEAD* option, where 'alive' and 'dead' are Tk named colours for alive and dead cells. For instance: 'red', 'blue', 'firebrick'... etc.
 
  Spaces are not allowed in the name, so use '-' instead.
  ```
  python carules.py -n DayAndNight --fill dark-violet:forest-green
  python caryules.py -r 368:245 -f medium-spring-green:grey -g 800 -c 20
  ```
  
  You can find a list of colours [here](http://wiki.tcl.tk/16166).
  
* Further explanations/help typing:
  ```
  python carules.py --help
  ```

Considerations
--------------

* To close the window send a keyboard interrupt (control + C).
* The window will close by itself when all the cells are dead.
* Launch the script inside ```carules``` directory, otherwise the window icon
won't load and Tkinter will crash.

Gallery
-------

* Download the gifs from [```ca-rules/gallery/```](https://github.com/7flying/ca-rules/tree/master/gallery).

Cool links
----------

* [Cellular Automata Rules Lexicon](http://psoup.math.wisc.edu/mcell/ca_rules.html)


Enjoy!
