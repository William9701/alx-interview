#!/usr/bin/python3
"""
island_perimeter module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Parameters:
    grid (List[List[int]]): A 2D list representing the map.
    0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.

    Assumptions:
    - Each cell is square, with a side length of 1.
    - Cells are connected horizontally/vertically (not diagonally).
    - The grid is rectangular, with its width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have “lakes”
      (water inside that isn’t connected to the water surrounding the island).
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land
                if r == 0 or grid[r-1][c] == 0:
                    # Water or grid edge to the North
                    perimeter += 1
                # Water or grid edge to the South
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:
                    # Water or grid edge to the West
                    perimeter += 1
                # Water or grid edge to the East
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
