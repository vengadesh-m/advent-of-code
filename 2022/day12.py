"""Day 12 solution"""
import os
import string
from collections import deque

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day12.txt"

def grid_alpha_to_num_converter(grid):
    "Convert the Grid of alphabets to its numbers starting 1 for a ending 26 for z"
    alphas = string.ascii_lowercase
    row = len(grid)
    col = len(grid[0])
    empty_grid = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            alpha = grid[i][j]
            if alpha in alphas:
                empty_grid[i][j] = ord(alpha) - 96
            if alpha == 'S':
                empty_grid[i][j] = 0
            if alpha == 'E':
                empty_grid[i][j] = 26
    return empty_grid


def shortest_path(queue, grid):
    "Find the shortest path with the grid and starting positions in the queue"
    positions = set()
    numbered_grid = grid_alpha_to_num_converter(grid)
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    while queue:
        (row, col), dist = queue.popleft()
        if (row, col) in positions:
            continue
        positions.add((row, col))
        if grid[row][col] == 'E':
            print("Shortest distance is:", dist)
            return
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        for row_direc, col_direc in directions:
            new_row = row + row_direc
            new_col = col + col_direc
            if (
                0 <= new_row < grid_rows and 0 <= new_col < grid_columns
                and
                numbered_grid[new_row][new_col] <= numbered_grid[row][col] + 1
            ):
                queue.append(((new_row, new_col), dist+1))


def part1(_f):
    "Solution for Part1"
    grid = [list(line) for line in _f.read().splitlines()]
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    queue = deque(
        ((i, j), 0)
        for i in range(grid_rows)
        for j in range(grid_columns)
        if grid[i][j] == 'S'
        )
    shortest_path(queue, grid)

def part2(_f):
    "Solution for part2"
    grid = [list(line) for line in _f.read().splitlines()]
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    queue = deque(
        ((i, j), 0)
        for i in range(grid_rows)
        for j in range(grid_columns)
        if grid[i][j] == 'a'
        )
    shortest_path(queue, grid)

with open(_file, encoding='utf-8') as _f:
    part1(_f)

with open(_file, encoding='utf-8') as _f:
    part2(_f)
