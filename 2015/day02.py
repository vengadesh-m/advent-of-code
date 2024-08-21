from input_reader import puzzle_input


def part1():
    wrapping_sheet = 0
    for i in puzzle_input():
        dimensions = i.split('x')
        dimensions = [int(i.strip('\n')) for i in dimensions]
        l, w, h = dimensions
        surface_dimensions = [l*w, w*h, h*l]
        surface_area = 2 * sum(surface_dimensions)
        result = surface_area + min(surface_dimensions)
        wrapping_sheet += result
    print(wrapping_sheet)


def part2():
    ribbon_length = 0
    for i in puzzle_input():
        dimensions = i.split('x')
        dimensions = [int(i.strip('\n')) for i in dimensions]
        l, w, h = dimensions
        shortest_perimeter = 2 * (sorted(dimensions)[0] + sorted(dimensions)[1])
        ribbon_length += shortest_perimeter + (l*w*h)
    print(ribbon_length)

part1()
part2()