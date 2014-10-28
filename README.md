CA-Rules!
=========

CA-Rules is a cellular automata command-line generation tool.

How to use
----------

####Automata Generation

* You can generate an automata giving its name.

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

####Other options

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
  
* Further explanations/help typing:
  ```
  python carules.py --help
  ```

Considerations
--------------

* To close the window send a keyboard interrupt (control + C).
* The window will close by itself when all the cells are dead.


Enjoy!
