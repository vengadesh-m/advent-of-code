
import os
import string

input_value = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day3.txt"

with open(file) as _file:
    for line in _file:
        input_value.append(line.strip("\n"))


def common_item(value):
    length = len(value)
    separator = int(length/2)
    first_part = value[:separator]
    second_part = value[separator:]
    for i in first_part:
        if second_part.count(i) >= 1:
            return i

common_items = [common_item(value) for value in input_value]

scores = {i: j for i, j in zip(string.ascii_letters, range(1, 53))}

result = [scores[item] for item in common_items]
print("Part 1:", sum(result))

def unique_item(values):
    elf1 = values[0]
    elf2 = values[1]
    elf3 = values[2]
    for value in elf1:
        if elf2.count(value) >= 1 and elf3.count(value) >= 1:
            return value
    
unique_items = [unique_item(input_value[i:i+3]) for i in range(0, len(input_value), 3)]
round_two = [scores[item] for item in unique_items]
print("Part 2:", sum(round_two))

