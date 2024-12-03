"Day 2 solution of AoC"
import re
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day3.txt"


with open(file, 'r', encoding='utf-8') as _file:
    for line in _file:
        result = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
    count = 0
    for i in result:
        numbers = re.findall("\d+", i)
        numbers = [int(i) for i in numbers]
        r = 1
        for num in numbers:
            r *= num
        count += r
    print(count)


def recursive_remove(result):
    dont_index = result.index("don't()")
    do_index = result.index("do()")
    if do_index < dont_index:
        del result[do_index]
    # print("dont_index: ", dont_index)
    # print("do_index: ", do_index)
    del result[dont_index:do_index+1]
    return result


with open(file, 'r', encoding='utf-8') as _file:
    for line in _file:
        result = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    count = 0
    while "don't()" in result:
        recursive_remove(result)
    count = 0
    for i in result:
        numbers = re.findall("\d+", i)
        numbers = [int(i) for i in numbers]
        r = 1
        for num in numbers:
            r *= num
        count += r
    print(count)
