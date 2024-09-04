import re

from input_reader import puzzle_input


def actual_chars(a):
    a = a.replace('\\"', 'a')
    a = a.replace('\\\\', 'a')
    special_char = re.findall(r'\\x[0-9a-z][0-9a-z]', a)
    for i in special_char:
        a = a.replace(i, 'a')
    return len(a)


def part1():
    total_chars = 0
    actual_characters = 0
    for i in puzzle_input():
        i = i.strip('\n')
        total_chars += len(i)
        print(i, actual_chars(i.strip('"')))
        actual_characters += actual_chars(i.strip('"'))
    # print(actual_characters)
    print(total_chars - actual_characters)


def escaped_count(a):
    actual_count = len(a)
    double_quotes_count = a.count('"')
    actual_count += double_quotes_count
    backslash_count = a.count('\\')
    actual_count += backslash_count
    return actual_count + 2


def part2():
    total_chars = 0
    escaped_chars = 0
    for i in puzzle_input():
        i = i.strip('\n')
        total_chars += len(i)
        # print(escaped_count(i))
        escaped_chars += escaped_count(i)
    print(escaped_chars-total_chars)

# part1()
part2()