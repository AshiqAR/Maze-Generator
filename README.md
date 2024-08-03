# Maze Generator and Solver

This repository contains Python scripts for generating and solving mazes using the union-find algorithm. The maze is visualized using the `turtle` module. The project is split into three files: `generateMaze.py`, `displayMaze.py`, and `mazeSolver.py`.

## Files

- `generateMaze.py`: Contains the code to generate a maze and save it to a file.
- `displayMaze.py`: Contains the code to visualize the generated maze.
- `mazeSolver.py`: Contains the code to read the maze from a file, solve it, and display the solution path as the cell numbers starting from 0 to rows\*colums-1.

## Usage

### Generating the Maze

Run the `generateMaze.py` script to generate a maze.

```bash
python generateMaze.py
```

You will be prompted to enter the number of rows and columns for the maze. The generated maze will be saved to `Generated_maze.txt`.

### Solving the Maze

Run the `mazeSolver.py` script to read the maze from `Generated_maze.txt`, solve it, and display the solution path.

```bash
python mazeSolver.py
```

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- `turtle` module (included with Python's standard library)
