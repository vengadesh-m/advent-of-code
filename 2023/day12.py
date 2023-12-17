"Day 12 solution of AoC"
import re
import os
from itertools import combinations

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day12.txt"


with open(file) as _f:
    ans = 0

    lines = _f.read().splitlines()
    for line in lines:
        chars, nums = line.split()
        nums = [int(x) for x in nums.split(",")]
        questions = [i for i, c in enumerate(chars) if c == "?"]
        # print(chars, nums, questions)
        for comb in combinations(questions, sum(nums) - chars.count("#")):
            a = "".join("#" if i in comb else c for i, c in enumerate(chars))
            lst = [len(t) for t in a.replace("?", ".").split(".") if t]
            if nums == lst:
                ans += 1
    print(ans)

with open(file) as _f:
    ans = 0

    lines = _f.read().splitlines()
    for line in lines:
        chars, nums = line.split()
        nums = [int(x) for x in nums.split(",")]
        questions = [i for i, c in enumerate(chars) if c == "?"]
        # print(chars, nums, questions)
        for comb in combinations(questions, sum(nums) - chars.count("#")):
            a = "".join("#" if i in comb else c for i, c in enumerate(chars))
            lst = [len(t) for t in a.replace("?", ".").split(".") if t]
            if nums == lst:
                ans += 1
    print(ans)