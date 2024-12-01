from input_reader import puzzle_input


def part1():
    data = []
    result = 0
    for i in puzzle_input():
        a = i.split(' ')
        data.append(int(f'{"-" if a[2] == "lose" else "+"}{a[3]}'))
    n = 7
    for i in range(0, (len(data) - n + 1), n):
        new_list = data[i:i+n]
        new_list.sort()
        print(new_list[-2:])
        result += sum(new_list[-2:])
    print(result)


part1()