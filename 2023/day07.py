"Day 6 solution of AoC"
import re
import os
from math import prod

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day07.txt"

def count_steps(steps, routes, step_count=0, next_step='AAA'):
    for step in steps:
        next_step = routes[next_step][1] if step == 'R' else routes[next_step][0]
        step_count += 1
        if next_step == 'ZZZ':
            return step_count
    if next_step != 'ZZZ':
        return count_steps(steps, routes, step_count, next_step)

with open(file) as _file:
    steps, routes = _file.read().split('\n\n')
    routes = routes.split('\n')
    routes = {
        route.split('=')[0].strip(): [i.strip(' \(').strip('\)') for i in route.split('=')[1].split(',')]
        for route in routes
    }
    print(count_steps(steps, routes))
