"""Day 10 solution"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day10.txt"


def part1(_f):
    "Solution for Part1"
    X = 1
    cycle = 1
    required_cycles = range(20, 260, 40)
    ans = 0

    for line in _f.read().split():
        cycle += 1
        try:
            if int(line):
                X += int(line)
        except ValueError:
            pass

        if cycle in required_cycles:
            ans += cycle * X
    print(f"Answer is {ans}")


def part2(_f):
    "Solution for Part2"
    X = 1
    cycle = 1
    sprite = [X-1, X, X+1]
    crt_position = range(241)
    cycle_sprite_map = {cycle: sprite}

    for line in _f.read().split():
        cycle += 1
        try:
            X += int(line)
            sprite = [X-1, X, X+1]
        except ValueError:
            pass
        cycle_sprite_map[cycle] = sprite
    # print(cycle_sprite_map)
    for crt in crt_position:
        if crt % 40 in cycle_sprite_map[crt+1]:
            print('#', end='')
        else:
            print('.', end='')
        if crt and (crt+1) % 40 == 0:
            print()

with open(_file) as _f:
    part1(_f)

with open(_file) as _f:
    part2(_f)
    