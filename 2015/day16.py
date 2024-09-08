from input_reader import puzzle_input

from itertools import combinations

# numbers = [1, 2, 3, 7, 7, 9, 10]
# a = itertools.combinations(numbers, 3)
# print(list(a))


def part1():
    data = puzzle_input("sample", 16)
    data = [int(i.strip('\n')) for i in data]
    print(data)
    target = 150
    result = [s for i in range(len(data), 0, -1) for s in combinations(data, i) if sum(s) == target]
    print(result)
    print(len(result))
    min_len = len(data)
    for i in result:
        if len(i) < min_len:
            min_len = len(i)

    result = [i for i in result if len(i) == min_len]
    print(len(result))

part1()