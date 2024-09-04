from itertools import groupby

from input_reader import puzzle_input


def lookandsay(n):
    return ''.join(str(len(list(g))) + k for k, g in groupby(n))


def part1():
    j = '3113322113'
    for i in range(50):
        j = lookandsay(j)
    print(len(j))


part1()