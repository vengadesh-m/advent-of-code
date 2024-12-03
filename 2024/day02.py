"Day 2 solution of AoC"
from copy import deepcopy
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day2.txt"


def conditioner(b):
    zero_count = b.count(0) != 0
    negative_count = len([i for i in b if i < 0]) == len(b)
    positive_count = len([i for i in b if i > 0]) == len(b)
    greater_than_3 = any([i > 3 for i in b if i > 0])
    negative_than_3 = any([i < -3 for i in b if i < 0])
    return zero_count or (not (negative_count or positive_count)) or greater_than_3 or negative_than_3


with open(file, 'r', encoding='utf-8') as _file:
    count = 0
    for line in _file:
        test_list = [int(i.strip('\n')) for i in line.split(' ')]
        b = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)]
        if not conditioner(b):
            count += 1

    print(count)

with open(file, 'r', encoding='utf-8') as _file:
    count = 0
    for line in _file:
        test_list = [int(i.strip('\n')) for i in line.split(' ')]
        b = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)]
        if not conditioner(b):
            count += 1
        else:
            for i in range(len(test_list)):
                tmp_b = deepcopy(test_list)
                tmp_b.pop(i)
                b = [tmp_b[i + 1] - tmp_b[i] for i in range(len(tmp_b) - 1)]
                if not conditioner(b):
                    count += 1
                    break
    print(count)
