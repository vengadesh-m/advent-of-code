from input_reader import puzzle_input


def part1():
    for i in puzzle_input():
        floor = 0
        for j in i:
            if j == ')':
                floor -= 1
            if j == '(':
                floor += 1
        print(floor)


def part2():
    for i in puzzle_input():
        count = 1
        floor = 0
        for j in i:
            if j == ')':
                floor -= 1
            if j == '(':
                floor += 1
            if floor == -1:
                print(count)
                break
            count += 1


part1()
part2()
