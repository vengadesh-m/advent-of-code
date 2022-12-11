"""Day 11 solution"""
import os
from copy import deepcopy
from math import prod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day11.txt"


def part1(_f):
    "Solution for Part1"
    monkey_map = {}
    for monkey in _f.read().split('\n\n'):
        monkey_map[monkey.split('\n', 1)[0].rstrip(':')] = {
            item.split(':')[0].strip(): [int(i) for i in item.split(':')[-1].strip().split(',')]
            if "Starting" in item.split(':')[0].strip()
            else item.split(':')[-1].strip()
            for item in monkey.split('\n', 1)[-1].split('\n')
            }

    for monkey, monkey_tricks in monkey_map.items():
        monkey_tricks.update(inspected_items=0)

    for _ in range(20):
        for monkey, monkey_tricks in monkey_map.items():
            items = deepcopy(monkey_tricks["Starting items"])
            for item in items:
                monkey_tricks["inspected_items"] += 1
                monkey_tricks["Starting items"].remove(item)
                new_worry = eval(
                    monkey_tricks["Operation"].split('=')[-1].replace('old', str(item))
                    )
                new_worry = int(new_worry/3)
                if new_worry % int(monkey_tricks["Test"].split()[-1]) == 0:
                    monkey_map[
                        f"Monkey {monkey_tricks['If true'].split()[-1]}"
                        ]["Starting items"].append(new_worry)
                else:
                    monkey_map[
                        f"Monkey {monkey_tricks['If false'].split()[-1]}"
                        ]["Starting items"].append(new_worry)

    print(
        f'Ans for part1 is {prod(sorted(i["inspected_items"] for i in monkey_map.values())[-2:])}'
        )


def part2(_f):
    "Solution for part2"
    monkey_map = {}
    for monkey in _f.read().split('\n\n'):
        monkey_map[monkey.split('\n', 1)[0].rstrip(':')] = {
            item.split(':')[0].strip(): [int(i) for i in item.split(':')[-1].strip().split(',')]
            if "Starting" in item.split(':')[0].strip()
            else item.split(':')[-1].strip()
            for item in monkey.split('\n', 1)[-1].split('\n')
            }

    for monkey, monkey_tricks in monkey_map.items():
        monkey_tricks.update(inspected_items=0)

    hcf = prod(int(m["Test"][-2:]) for m in monkey_map.values()) 
    # Highest common factor for easy divide

    for _ in range(10000):
        for monkey, monkey_tricks in monkey_map.items():
            items = deepcopy(monkey_tricks["Starting items"])
            for item in items:
                monkey_tricks["inspected_items"] += 1
                monkey_tricks["Starting items"].remove(item)
                new_worry = eval(
                    monkey_tricks["Operation"].split('=')[-1].replace('old', str(item))
                    )
                new_worry = new_worry % hcf
                if new_worry % int(monkey_tricks["Test"].split()[-1]) == 0:
                    monkey_map[
                        f"Monkey {monkey_tricks['If true'].split()[-1]}"
                        ]["Starting items"].append(new_worry)
                else:
                    monkey_map[
                        f"Monkey {monkey_tricks['If false'].split()[-1]}"
                        ]["Starting items"].append(new_worry)

    print(
        f'Ans for part2 is {prod(sorted(i["inspected_items"] for i in monkey_map.values())[-2:])}'
        )


with open(_file, encoding='utf-8') as _f:
    part2(_f)
