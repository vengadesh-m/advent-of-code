"Day 6 solution of AoC"
import re
import os
from math import prod

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day06.txt"

with open(file) as _file:
    lines = _file.read()
    _, times, distances = re.split(r'Time:|Distance:', lines)
    times = [int(time) for time in times.split()]
    distances = [int(distance) for distance in distances.split()]
    result = []
    for t, d in zip(times, distances):
        count = 0
        for bt in range(t+1):
            dt = bt * (t - bt)
            if dt > d:
                count +=1 
        result.append(count)
    print(prod(result))