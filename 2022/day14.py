"""Day 12 solution"""
import os
from itertools import product

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day14.txt"


def rock_tiles(line):
    rock_tiles = []
    tiles = [item.strip().split(',') for item in line.split('->')]
    # print("Tiles", tiles)
    for i, tile in enumerate(tiles):
        ft = tile
        if i+1 == len(tiles):
            break
        st = tiles[i+1]
        # print(f"First tile {ft}, Second tile {st}")
        ft0, ft1 = [int(i) for i in ft]
        st0, st1 = [int(i) for i in st]
        x = [*range(ft0, st0+1 if st0 >= ft0 else st0-1, 1 if st0 >= ft0 else -1)]
        y = [*range(ft1, st1+1 if st1 >= ft1 else st1-1, 1 if st1 >= ft1 else -1)]
        # print(x, y)
        for i in product(x, y):
            rock_tiles.append(i)
    # print("Rock tiles", rock_tiles)
    return rock_tiles

def sand_counter(rock_tile, bottom, no_bottom=True):
    x = 0
    while True:
        start_tile = (500, 0)
        while True:
            i, j = start_tile
            if j+1 >= bottom and no_bottom:
                return x
            if (i, j+1) not in rock_tile:
                start_tile = (i, j+1)
            elif (i-1, j+1) not in rock_tile:
                start_tile = (i-1, j+1)
            elif (i+1, j+1) not in rock_tile:
                start_tile = (i+1, j+1)
            else:
                break
        if start_tile == (500, 0):
            return x+1
        rock_tile.add(start_tile)
        x += 1

def part1(_f):
    lines = _f.read().splitlines()
    rock_tile = set()
    for line in lines:
        for rock in rock_tiles(line):
            rock_tile.add(rock)
    bottom = max(i[1] for i in rock_tile)+2
    print(f"Answer for Part 1: {sand_counter(rock_tile, bottom)}")


def part2(_f):
    lines = _f.read().splitlines()
    rock_tile = set()
    for line in lines:
        for rock in rock_tiles(line):
            rock_tile.add(rock)
    infinite_x = [*range(-10000, 10000)]
    bottom = max(i[1] for i in rock_tile)+2
    for i in product(infinite_x, [bottom]):
        rock_tile.add(i)
    print("Answer for Part2", sand_counter(rock_tile, bottom, False))


with open(_file, encoding="utf-8") as _f:
    part1(_f)


with open(_file, encoding="utf-8") as _f:
    part2(_f)
