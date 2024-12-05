"Day 2 solution of AoC"
import functools
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day5.txt"


def part1():
    rules, sections = open(file).read().split("\n\n")
    rules = rules.split("\n")
    sections = sections.split("\n")

    pages = [[int(i) for i in section.split(',')] for section in sections]
    rules = [[int(i) for i in rule.split('|')] for rule in rules]
    result = sum(search(page, rules) for page in pages)
    print(result)


def part2():
    rules, sections = open(file).read().split("\n\n")
    rules = rules.split("\n")
    sections = sections.split("\n")

    pages = [[int(i) for i in section.split(',')] for section in sections]
    rules = [[int(i) for i in rule.split('|')] for rule in rules]
    result = 0
    for page in pages:
        if search(page, rules) == 0:
            page.sort(key=functools.cmp_to_key(lambda a, b: check_pair(a, b, rules)))
            result += page[len(page)//2]
    print(result)


def search(page, rules):
    for i, j in rules:
        try:
            if page.index(i) >= page.index(j):
                return 0
        except ValueError:
            pass
    return page[len(page)//2]


def check_pair(i, j, rules):
    if [i, j] in rules:
        return -1
    elif [j, i] in rules:
        return 1
    else:
        return 0


part1()
part2()