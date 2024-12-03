"""Day 20 solution"""
import os
import re
from itertools import chain, repeat

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day21.txt"


def resolve_exp(root_value, monkeys):
    fv, op, sv = root_value.split()
    return f"\({monkeys[fv]}\) {op} \({monkeys[sv]}\)"

def part1(_f):
    values = _f.read().splitlines()
    monkeys = {}


    for i in values:
        if y := re.findall(r'\d+', i):
            monkeys[i.split(':')[0]] = int(y[0])
        else:
            monkeys[i.split(':')[0]] = i.split(':')[-1].strip()
    print(monkeys)

    print(resolve_exp(monkeys["root"], monkeys))


    
with open(_file) as _f:
    part1(_f)




from operator import add, mul, sub, truediv

flip = lambda f: lambda *a: f(*reversed(a))

OPERATIONS = {
    "+": (add, sub, sub),
    "-": (sub, add, flip(sub)),
    "*": (mul, truediv, truediv),
    "/": (truediv, mul, flip(truediv)),
}


def parse(f):
    vals = {}
    for line in f:
        name, eq = line.split(": ")
        match eq.split():
            case [num]:
                vals[name] = int(num)
            case [a, op, b]:
                vals[name] = a, b, *OPERATIONS[op]
    return vals


def calc(vals, i):
    match vals[i]:
        case a, b, f, _, _:
            av, bv = calc(vals, a), calc(vals, b)
            if None in (av, bv):
                return None
            return f(av, bv)
        case _:
            return vals[i]


def p1(f):
    vals = parse(f)
    return int(calc(vals, "root"))


def p2(f):
    vals = parse(f)
    vals["humn"] = None
    vals["root"] = *vals["root"][:2], *OPERATIONS["-"]

    def solve(i, val):
        match vals[i]:
            case a, b, _, fa, fb:
                match calc(vals, a), calc(vals, b):
                    case av, None:
                        return solve(b, fb(val, av))
                    case None, bv:
                        return solve(a, fa(val, bv))
            case None:
                return val

    return int(solve("root", 0))

with open(_file) as _f:
    print(p2(_f))