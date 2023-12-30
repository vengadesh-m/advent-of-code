"Day 19 solution of AoC"
import re
import os
from itertools import combinations

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day19.txt"


with open(file) as _f:
    ans = _f.read().splitlines()
    print(ans)