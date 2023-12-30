"Day 2 solution of AoC"
import re
import os

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day2.txt"

with open(file) as _f:
    result = 0
    for line in _f:
        game_num = int(re.findall('\d+', line.split(':')[0])[0])
        if (max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ red*', line)]) <= 12 and
            max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ green*', line)]) <= 13 and
            max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ blue*', line)]) <= 14):
            result += game_num
    print(result)

with open(file) as _f:
    result = 0
    for line in _f:
        red = max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ red*', line.split(':')[-1])])
        green = max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ green*', line.split(':')[-1])])
        blue = max([int(re.findall('\d+', i)[0]) for i in re.findall(r'\d+ blue*', line.split(':')[-1])])
        result += red * green * blue
    print(result)

