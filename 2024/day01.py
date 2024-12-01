"Day 1 solution of AoC"
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day1.txt"

with open(file, 'r', encoding='utf-8') as _file:
    results = []
    first_list = []
    second_list = []
    for line in _file:
        a, b = line.split('   ')
        b = b.strip('\n')
        first_list.append(int(a))
        second_list.append(int(b))
    # print(sorted(first_list), sorted(second_list))
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    for i in range(len(first_list)):
        results.append(abs(second_list[i] - first_list[i]))
    print(sum(results))

with open(file, 'r', encoding='utf-8') as _file:
    results = []
    first_list = []
    second_list = []
    for line in _file:
        a, b = line.split('   ')
        b = b.strip('\n')
        first_list.append(int(a))
        second_list.append(int(b))
    for i in first_list:
        results.append(i * second_list.count(i))
    print(sum(results))
