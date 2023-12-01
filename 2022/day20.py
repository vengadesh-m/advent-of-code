"""Day 20 solution"""
import os
import re
from itertools import chain, repeat

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day20.txt"

def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))

class ShiftableList(list):

    def shift(self, item):
        old_index = self.index(item)
        if old_index + item >= len(self):
            new_index = (old_index + item + 1) % len(self)
        else:
            new_index = old_index + item
        if new_index == 0:
            new_index = len(self) - 1
        self.remove(item)
        self.insert(new_index, item)


def part1(_f):
    initial = [int(item) for item in _f.read().splitlines()]
    shiftable_list = ShiftableList(initial)

    for item in initial:
        shiftable_list.shift(item)
    
    circular = list(ncycles(shiftable_list, 1000))
    ind_of_first_zero = circular.index(0)
    ans = circular[1000 % len(initial)] + circular[2000 % len(initial)] + circular[3000 % len(initial)]

    print(ans)

with open(_file) as _f:
    part1(_f)




from collections import deque, namedtuple

_ = namedtuple("_", ("id", "val"))


def p1(f):
    nums = deque(_(id, int(x)) for id, x in enumerate(f))
    order = list(nums)

    for x in order:
        idx = next(i for i, y in enumerate(nums) if x.id == y.id)
        nums.rotate(-idx)
        nums.popleft()
        nums.rotate(-x.val)
        nums.appendleft(x)

    nums.rotate(-next(i for i, x in enumerate(nums) if x.val == 0))
    return nums[1000 % len(nums)].val + nums[2000 % len(nums)].val + nums[3000 % len(nums)].val


def p2(f):
    nums = deque(_(id, int(x) * 811589153) for id, x in enumerate(f))
    order = list(nums)

    for t in range(10):
        for x in order:
            idx = next(i for i, y in enumerate(nums) if x.id == y.id)
            nums.rotate(-idx)
            nums.popleft()
            nums.rotate(-x.val)
            nums.appendleft(x)

    nums.rotate(-next(i for i, x in enumerate(nums) if x.val == 0))
    return nums[1000 % len(nums)].val + nums[2000 % len(nums)].val + nums[3000 % len(nums)].val


with open(_file) as _f:
    print(p2(_f))