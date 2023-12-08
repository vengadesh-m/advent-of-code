"Day 3 solution of AoC"
import re
import os
from collections import defaultdict

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day3.txt"

with open(file) as _f:
    result = 0
    lines = _f.read().splitlines()
    for line_num, line in enumerate(lines):
        for item in re.finditer('\d+', line):
            indices = [(line_num, item.start() - 1), (line_num, item.end())]
            indices += [(line_num - 1, j) for j in range(item.start() - 1, item.end() + 1)]
            indices += [(line_num + 1, j) for j in range(item.start() - 1, item.end() + 1)]
            count = sum(0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "." for a, b in indices)
            if count > 0:
                result += int(item.group())
    print(result)


with open(file) as _f:
    result = 0
    lines = _f.read().splitlines()
    adj = defaultdict(list)
    for line_num, line in enumerate(lines):
        for item in re.finditer('\d+', line):
            indices = [(line_num, item.start() - 1), (line_num, item.end())]
            indices += [(line_num - 1, j) for j in range(item.start() - 1, item.end() + 1)]
            indices += [(line_num + 1, j) for j in range(item.start() - 1, item.end() + 1)]
            for a, b in indices:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != ".":
                    adj[a, b].append(item.group())
    print(sum(int(x[0]) * int(x[-1]) for x in adj.values() if len(x) == 2))