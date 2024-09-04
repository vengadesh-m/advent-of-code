from input_reader import puzzle_input
import re

total_grid = {}


for i in range(1000):
    for j in range(1000):
        total_grid[(i, j)] = 0


def action(start_coordinate, end_coordinate, action):
    for i in range(int(start_coordinate[0]), int(end_coordinate[0])+1):
        for j in range(int(start_coordinate[1]), int(end_coordinate[1])+1):
            if action == 'turn on':
                total_grid[(i, j)] = 1
            if action == 'turn off':
                total_grid[(i, j)] = 0
            if action == 'toggle':
                total_grid[(i, j)] = abs(total_grid[i, j] - 1)


def action_part2(start_coordinate, end_coordinate, action):
    for i in range(int(start_coordinate[0]), int(end_coordinate[0])+1):
        for j in range(int(start_coordinate[1]), int(end_coordinate[1])+1):
            if action == 'turn on':
                total_grid[(i, j)] += 1
            if action == 'turn off' and total_grid[(i, j)] > 0:
                total_grid[(i, j)] -= 1
            if action == 'toggle':
                total_grid[(i, j)] += 2


def get_numbers(a):
    b = re.findall(r'[0-9]+,[0-9]+ .* [0-9]+,[0-9]+', a)
    return [tuple(i.split(',')) for i in b[0].split(' through ')]


def part1():
    for i in puzzle_input():
        if 'turn on' in i:
            a = get_numbers(i)
            action(a[0], a[1], 'turn on')
        if 'turn off' in i:
            a = get_numbers(i)
            action(a[0], a[1], 'turn off')
        if 'toggle' in i:
            a = get_numbers(i)
            action(a[0], a[1], 'toggle')
    print(len([x for x in total_grid.values() if x == 1]))


def part2():
    for i in puzzle_input():
        if 'turn on' in i:
            a = get_numbers(i)
            action_part2(a[0], a[1], 'turn on')
        if 'turn off' in i:
            a = get_numbers(i)
            action_part2(a[0], a[1], 'turn off')
        if 'toggle' in i:
            a = get_numbers(i)
            action_part2(a[0], a[1], 'toggle')
    print(sum(total_grid.values()))


# part1()
part2()
