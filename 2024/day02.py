"Day 1 solution of AoC"
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day2.txt"

with open(file, 'r', encoding='utf-8') as _file:
    for line in _file:
        print(line)
