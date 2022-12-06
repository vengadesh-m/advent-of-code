"Day 6 solution"
import os
from collections import deque

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day6.txt"

with open(_file, encoding='utf-8') as _f:
    input_value = _f.read()

def find_first_signal(marker_count):
    "Return the Start of the marker"
    queue = deque(maxlen=marker_count)
    for num, value in enumerate(input_value):
        queue.append(value)
        if len(queue) == marker_count and len(set(queue)) == marker_count:
            return num + 1
    return None


print("Answer to Part 1 is: ", find_first_signal(4))
print("Answer to Part 2 is: ", find_first_signal(14))
