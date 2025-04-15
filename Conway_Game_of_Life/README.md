# Conway's Game of Life
### Szymon Mirczak side project

## Overviev
The Game of Life by the British mathematician John Horton Conway isn’t a game in the traditional sense. In technical terms, it’s a cellular automaton, but you can think of Game of Life as a simulation whose evolution depends on its initial state and doesn’t require further input from any players.

## Rules
The game’s board is an infinite, two-dimensional grid of cells. Each cell can be in one of two possible states:

* Alive
* Dead

Each cell evolves to the next generation depending on the state of itself and its neighbor cells. Here’s a summary of the evolution rules:

* Alive cells die if they have fewer than two (underpopulation) or more than three living neighbors (overpopulation).
* Alive cells stay alive if they have two or three living neighbors.
* Dead cells with exactly three living neighbors become alive (reproduction).

The game’s initial state is the seed, or initial life pattern. In this implementation, the life pattern will be a set of alive cells. The first generation results from applying the above rules to every cell in the seed. The second generation results from applying the rules to the first generation, and so on. So, each generation is a pure function of the preceding one.

The challenge in this project is to program the evolution algorithm in Python and then provide a command-line interface (CLI) to run the game with different life patterns.

## Rules
* 