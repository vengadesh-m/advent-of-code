"Day 9 solution"
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day9.txt"

def direction_map(direc, element):
    match direc:
        case "R":
            return [element[0]+ 1, element[1]]
        case "U":
            return [element[0], element[1]+1]
        case "L":
            return [element[0]-1, element[1]]
        case "D":
            return [element[0], element[1]-1]

def follower(direc, e):
    match direc:
        case "R":
            return [e[0]-1, e[1]]
        case "U":
            return [e[0], e[1]-1]
        case "L":
            return [e[0]+1, e[1]]
        case "D":
            return [e[0], e[1]+1]

def tails_path(tail_start, tail_end):
    path = []
    for i, j in zip(range(tail_start[0], tail_end[0]), range(tail_start[1], tail_end[1]+1)) :
        path.append([i, j])
    return path

def part1(_f):
    head = [0,0]
    tail = [0,0]
    position = set()
    for line in _f.read().splitlines():
        direction, steps = line.split()

        for _ in range(int(steps)):
            head = direction_map(direction, head)
        tail = follower(direction, head)
        tails_path
        print(head, tail)
        position.add(tuple(tail))
    print(position)
    print(f"Answer of Part 1 is {len(position)}")
