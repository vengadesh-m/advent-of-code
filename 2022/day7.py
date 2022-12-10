"""Day 7 solution"""
import os
from pathlib import Path
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day7.txt"


def part1(_f):
    cwd = Path("/")
    dirs = defaultdict(int)

    for line in _f.read().splitlines():
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    dirs[path] += size

    return sum(x for x in dirs.values() if x <= 100000)

with open(_file, encoding='utf-8') as _f:
    print(part1(_f))
