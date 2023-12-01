"Day 1 solution of AoC"
import os

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day1.txt"

with open(file, 'r', encoding='utf-8') as _file:
    result = 0
    for line in _file:
        digits = [i for i in line if i.isdigit()]
        result += int(digits[0] + digits[-1])
    print(result)

def find_first_and_last_number(line):
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    found_items = {line.index(item): item  for item in items if item in line}
    return found_items[min(found_items.keys())], found_items[max(found_items.keys())]

with open(file, 'r', encoding='utf-8') as _file:
    result = 0
    decoder = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five':'5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in _file:
        first, last = find_first_and_last_number(line)
        result += int(decoder.get(first, first) + decoder.get(last, last))
    print(result)

