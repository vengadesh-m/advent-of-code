"Day 1 solution of AoC"
import os

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day1.txt"

with open(file, 'r', encoding='utf-8') as _file:
    VALUE = 0
    COUNTER = 0
    for line in _file:
        if line != "\n":
            VALUE += int(line.rstrip("\n"))
        else:
            result[COUNTER] = VALUE
            VALUE = 0
            COUNTER += 1

print("Max calories held by the leading Elf is (answer for part 1) ", max(result.values()))

print(
    "Max calories held by the top three Elfs are (answer for part 2) ",
    sum(sorted(result.values(), reverse=True)[:3])
    )
