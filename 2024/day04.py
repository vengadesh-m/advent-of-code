"Day 2 solution of AoC"
import re
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day4.txt"


with open(file, 'r', encoding='utf-8') as _file:
    grid = []

    for line in _file:
        line = line.strip('\n')
        grid.append(list(line))
    directions = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for di, dj in directions:
                if not (0 <= i + 3 * di < len(grid) and 0 <= j + 3 * dj < len(grid[0])):
                    continue
                if (grid[i][j] == 'X' and grid[i+di][j+dj] == 'M' and grid[i+2*di][j+2*dj] == 'A' and grid[i+3*di][j+3*dj] == 'S'):
                    count += 1
    print(count)


with open(file, 'r', encoding='utf-8') as _file:
    grid = []

    for line in _file:
        line = line.strip('\n')
        grid.append(list(line))
    directions = [(1,1), (2,2), (0,2), (2,0)]
    count = 0
    x_mas = ["MASSM", "MASMS", "SAMSM", "SAMMS"]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not (0 <= i + 2 < len(grid) and 0 <= j + 2 < len(grid[0])):
                continue
            for x in x_mas:
                if (grid[i][j] == x[0] and
                grid[i + directions[0][0]][j + directions[0][1]] == x[1] and
                grid[i + directions[1][0]][j + directions[1][1]] == x[2] and
                grid[i + directions[2][0]][j + directions[2][1]] == x[3] and
                grid[i + directions[3][0]][j + directions[3][1]] == x[4]):
                    count += 1
    print(count)
