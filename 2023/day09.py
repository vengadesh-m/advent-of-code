"Day 9 solution of AoC"
import re
import os
from math import prod

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day09.txt"


with open(file) as _f:
    lines = _f.read().splitlines()
    result = []
    for line in lines:
        items = line.split()
        items = [int(item) for item in items]
        last_items = [items[-1]]
        while any(items):
            items = [items[i+1]-items[i] for i in range(len(items)) if i+1 < len(items)]
            last_items.append(items[-1])
            # print(items)
        result.append(sum(last_items))
    print(sum(result))

def find_result(items):
    # print(result)
    return sum([-item if num%2 != 0 else item  for num, item in enumerate(items)])


with open(file) as _f:
    lines = _f.read().splitlines()
    result = []
    for line in lines:
        items = line.split()
        items = [int(item) for item in items]
        last_items = [items[0]]
        while any(items):
            items = [items[i+1]-items[i] for i in range(len(items)) if i+1 < len(items)]
            last_items.append(items[0])
            # print(items)
        # print(find_result(last_items))
        result.append(find_result(last_items))
    print(sum(result))
