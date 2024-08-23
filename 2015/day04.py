from input_reader import puzzle_input
import hashlib


def md5_hash(string):
  """Calculates the MD5 hash of a string."""
  return hashlib.md5(string.encode()).hexdigest()


def part1():
    inp = 'abcdef'
    for i in range(10000000):
        inp = 'ckczppom' + str(i)
        # print(inp)
        # print(md5_hash('abcdef609043'))
        if md5_hash(inp).startswith('000000'):
            print(i)
            break

def part2():
    for i in puzzle_input():
        x, y = 0, 0
        a, b = 0, 0
        starting_positions = [(x, y)]
        for num, j in enumerate(i):
            if num % 2 == 0:
                if j == '>':
                    x += 1
                if j == 'v':
                    y -= 1
                if j == '<':
                    x -= 1
                if j == '^':
                    y += 1
                starting_positions.append((x, y))
            else:
                if j == '>':
                    a += 1
                if j == 'v':
                    b -= 1
                if j == '<':
                    a -= 1
                if j == '^':
                    b += 1
                starting_positions.append((a, b))
        print(len(set(starting_positions)))
part1()
# part2()
