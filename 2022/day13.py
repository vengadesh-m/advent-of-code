"""Day 12 solution"""
import os
from itertools import zip_longest
from functools import cmp_to_key


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day13.txt"


def sort_compare(a, b):
    print(a, b)
    if isinstance(a, list) and isinstance(b, list):
        for i, j in zip_longest(a, b):
            print(i, j)
            if isinstance(i, list) and isinstance(j, list):
                print("Lists found", i, j)
                result = compare(i, j)
                if result is None:
                    continue
                return result
            if isinstance(i, list) and not isinstance(j, list):
                print("Only one list found. Converting", i , j)
                if j:
                    j = [j]
                else:
                    return -1
                return compare(i, j)
            if not isinstance(i, list) and isinstance(j, list):
                print("Only one list found. Converting", i , j)
                if i:
                    i = [i]
                else:
                    return 1
                i = [i]
                return compare(i, j)
            if i == j:
                print("Same value continuing", i , j)
                return 0
            if not i and (j or j == 0):
                print("First element is not found", i, j)
                print("Right order", i, j)
                return 1
            if (i or i == 0) and not j:
                print("Second element is not found", i, j)
                print("Not right order", i, j)
                return -1
            if i < j:
                print("Right order", i, j, "returning True")
                return -1
            if i > j:
                print("Not right order", i, j)
                return 1

def compare(a, b):
    print(a, b)
    if isinstance(a, list) and isinstance(b, list):
        for i, j in zip_longest(a, b):
            print(i, j)
            if isinstance(i, list) and isinstance(j, list):
                print("Lists found", i, j)
                result = compare(i, j)
                if result is None:
                    continue
                return result
            if isinstance(i, list) and not isinstance(j, list):
                print("Only one list found. Converting", i , j)
                if j:
                    j = [j]
                else:
                    return False
                result = compare(i, j)
                if result is None:
                    continue
                return result
            if not isinstance(i, list) and isinstance(j, list):
                print("Only one list found. Converting", i , j)
                if i:
                    i = [i]
                else:
                    return True
                i = [i]
                result = compare(i, j)
                if result is None:
                    continue
                return result
            if i == j:
                print("Same value continuing", i , j)
                continue
            if not i and (j or j == 0):
                print("First element is not found", i, j)
                print("Right order", i, j)
                return 1
            if (i or i == 0) and not j:
                print("Second element is not found", i, j)
                print("Not right order", i, j)
                return -1
            if i < j:
                print("Right order", i, j, "returning True")
                return -1
            if i > j:
                print("Not right order", i, j)
                return 1

def part1(_f):
    "Solution for part 1"
    counter = 0
    input = []
    temp = _f.read().split('\n\n')
    for i in temp:
        for j in i.split('\n'):
            input.append(eval(j))

    for i in range(0, len(input), 2):
        if (compare(input[i], input[i+1])) == 1:
            print(input[i], input[i+1], " has right order")
            counter = counter + (i+2)//2
    print("Counter value to", counter)


def part2(_f):
    temp = _f.read().splitlines()
    temp = [eval(i) for i in temp if i]
    temp.append([[2]])
    temp.append([[6]])
    print(sorted(temp, key=cmp_to_key(sort_compare)))

with open(_file, encoding='utf-8') as _f:
    part2(_f)
