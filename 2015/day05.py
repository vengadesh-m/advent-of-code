from input_reader import puzzle_input


def vowels_count(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in a:
        if i in vowels:
            count += 1
    return count >= 3


def double_chars(a):
    doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk',
               'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv',
               'ww', 'xx', 'yy', 'zz']
    for i in doubles:
        if i in a:
            return True
    return False


def disallwed_words(a):
    disallowed = ['ab', 'cd', 'pq', 'xy']
    for i in disallowed:
        if i in a:
            return True
    return False


def duplicate_finds(a):
    for i in range(len(a)):
        j = i+2
        finder = a[i:j]
        if finder in a[j:]:
            return True
    return False


def repeating(a):
    for i in range(len(a)):
        j = i + 2
        if j < len(a) and a[i] == a[j]:
            return True
    return False


def part1():
    result = 0
    for i in puzzle_input():
        if vowels_count(i) and double_chars(i) and not disallwed_words(i):
            result += 1
    print(result)


def part2():
    result = 0
    for i in puzzle_input():
        print(duplicate_finds(i), repeating(i))
        if duplicate_finds(i) and repeating(i):
            result += 1
    print(result)


# part1()
part2()
