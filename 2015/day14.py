import re
import math
from input_reader import puzzle_input


def combinations_summing_to_100():
    result = []
    for i in range(0, 101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                l = 100 - i - j - k
                result.append((i, j, k, l))
    return result


def part1():
    data = []
    results = []
    for i in puzzle_input("actual", '14'):
        data.append([int(i) for i in re.findall(r'-?\d+', i)])
    print(data)
    capacity = [i[0] for i in data]
    durability = [i[1] for i in data]
    flavor = [i[2] for i in data]
    texture = [i[3] for i in data]
    calories = [i[4] for i in data]
    for k in combinations_summing_to_100():
        a = 0 if (sum(k[i] * capacity[i] for i in range(4))) < 0 else (sum(k[i] * capacity[i] for i in range(4)))
        b = 0 if (sum(k[i] * durability[i] for i in range(4))) < 0 else (sum(k[i] * durability[i] for i in range(4)))
        c = 0 if (sum(k[i] * flavor[i] for i in range(4))) < 0 else (sum(k[i] * flavor[i] for i in range(4)))
        d = 0 if (sum(k[i] * texture[i] for i in range(4))) < 0 else (sum(k[i] * texture[i] for i in range(4)))
        # print(a, b, c, d)
        out = a * b * c * d
        # print(i, 100-i, out)
        results.append(
            out
        )
    print(max(results))


def part2():
    data = []
    results = []
    for i in puzzle_input("actual", '14'):
        data.append([int(i) for i in re.findall(r'-?\d+', i)])
    print(data)
    capacity = [i[0] for i in data]
    durability = [i[1] for i in data]
    flavor = [i[2] for i in data]
    texture = [i[3] for i in data]
    calories = [i[4] for i in data]
    for k in combinations_summing_to_100():
        a = 0 if (sum(k[i] * capacity[i] for i in range(4))) < 0 else (sum(k[i] * capacity[i] for i in range(4)))
        b = 0 if (sum(k[i] * durability[i] for i in range(4))) < 0 else (sum(k[i] * durability[i] for i in range(4)))
        c = 0 if (sum(k[i] * flavor[i] for i in range(4))) < 0 else (sum(k[i] * flavor[i] for i in range(4)))
        d = 0 if (sum(k[i] * texture[i] for i in range(4))) < 0 else (sum(k[i] * texture[i] for i in range(4)))
        e = 0 if (sum(k[i] * calories[i] for i in range(4))) < 0 else (sum(k[i] * calories[i] for i in range(4)))
        out = a * b * c * d
        # print(i, 100-i, out)
        if e == 500:
            results.append(
                out
            )
    print(max(results))


part1() #21367368
part2() #1766400
