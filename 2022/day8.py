"Day 9 solution"
import os
import numpy as np
from math import sqrt, prod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day8.txt"

def part1(_f):
    input_list = list(row  for line in _f.read().splitlines() for row in line)
    matrix_length = int(sqrt(len(input_list)))
    array = np.array(input_list).reshape((matrix_length,matrix_length))
    inner_matrix_length = len(array[1:-1, 1:-1])
    ans = matrix_length*matrix_length - inner_matrix_length*inner_matrix_length
    for row in  range(1,matrix_length-1):
        for col in range(1,matrix_length-1):
            top = [int(array[row_count][col]) for row_count in range(row)]
            bottom = [int(array[row_count][col]) for row_count in range(row+1, matrix_length)]
            left = [int(array[row][col_count]) for col_count in range(col)]
            right = [int(array[row][col_count]) for col_count in range(col+1, matrix_length)]
            element = int(array[row][col])
            if element > max(top) or element > max(bottom) or element > max(right) or element > max(left):
                ans += 1
    print(f"{ans} no. of trees is visible")


def element_counter(l, element, reverse=False):
    if reverse:
        l = reversed(l)
    counter = 0
    for i in l:
        if element > i:
            counter += 1
        elif element == i:
            counter += 1
            return counter
        else:
            counter += 1
            return counter
    return counter


def part2(_f):
    input_list = list(row  for line in _f.read().splitlines() for row in line)
    matrix_length = int(sqrt(len(input_list)))
    array = np.array(input_list).reshape((matrix_length,matrix_length))
    ans = []
    for row in  range(1,matrix_length-1):
        for col in range(1,matrix_length-1):
            top = [int(array[row_count][col]) for row_count in range(row)]
            bottom = [int(array[row_count][col]) for row_count in range(row+1, matrix_length)]
            left = [int(array[row][col_count]) for col_count in range(col)]
            right = [int(array[row][col_count]) for col_count in range(col+1, matrix_length)]
            element = int(array[row][col])
            ans.append(
                element_counter(top, element, reverse=True) *
                element_counter(bottom, element) * 
                element_counter(left, element, reverse=True) * 
                element_counter(right, element)
                )            
    print(f"{max(ans)} is the highest score")


with open(_file, encoding="utf-8") as _f:
    part1(_f)

with open(_file, encoding="utf-8") as _f:
    part2(_f)
