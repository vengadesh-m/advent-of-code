"Day 11 solution of AoC"
import re
import os
from itertools import combinations

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day11.txt"


with open(file) as _f:
    grid = [line.strip() for line in _f]
    x = {i for i, line in enumerate(grid) if "#" not in line}
    y = {j for j in range(len(grid[0])) if "#" not in [line[j] for line in grid]}
    pts = {(i+sum([i>a for a in x]), j+sum([j>b for b in y])) for i, l in enumerate(grid) for j, c in enumerate(l) if c == "#"}
    print(sum([abs(i[0]-j[0]) + abs(i[1]-j[1]) for i,j in combinations(pts, 2)]))

with open(file) as _f:
    grid = [line.strip() for line in _f]
    x = {i for i, line in enumerate(grid) if "#" not in line}
    y = {j for j in range(len(grid[0])) if "#" not in [line[j] for line in grid]}
    pts = {(i+(sum([i>a for a in x])*999999), j+(sum([j>b for b in y])*999999)) for i, l in enumerate(grid) for j, c in enumerate(l) if c == "#"}
    print(sum([abs(i[0]-j[0]) + abs(i[1]-j[1]) for i,j in combinations(pts, 2)]))