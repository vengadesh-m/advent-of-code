"Day 4 solution of AoC"
import os
import string

input_value = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day4.txt"

with open(file, encoding="utf-8") as _file:
    for line in _file:
        input_value.append(line.strip("\n"))


counter = 0
for value in input_value:
    containers = value.split(',')
    first_container = list(range(int(containers[0].split('-')[0]), int(containers[0].split('-')[-1])+1))
    second_container = list(range(int(containers[1].split('-')[0]), int(containers[1].split('-')[-1])+1))
    if all(value in second_container for value in first_container) or all(value in first_container for value in second_container):
        counter += 1

print(counter)

overlaps = 0

for value in input_value:
    containers = value.split(',')
    first_container = list(range(int(containers[0].split('-')[0]), int(containers[0].split('-')[-1])+1))
    second_container = list(range(int(containers[1].split('-')[0]), int(containers[1].split('-')[-1])+1))
    if any(value in second_container for value in first_container) or any(value in first_container for value in second_container):
        overlaps += 1

print(overlaps)