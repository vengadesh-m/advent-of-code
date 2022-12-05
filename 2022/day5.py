import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day5.txt"




test1 = ["N", "Z"]
test2 = ["D", "C", "M"]
test3 = ["P"]

input_stack = [
    [*"DZTH"], 
    [*"SCGTWRQ"],
    [*"HCRNQFBP"],
    [*"ZHFNCL"],
    [*"SQFLG"],
    [*"SCRBZWPV"], 
    [*"JFZ"],
    [*"QHRZVLD"], 
    [*"DLZFNGHB"]
]
input_stack = [
[*"RWFHTS"], [*"WQDGS"], [*"WTB"], [*"JZQNTWRD"], [*"ZTVLGHBF"], [*"GSBVCTPL"], [*"PGWTRBZ"], [*"RJCTMGN"], [*"WBGL"]
]
# print(input_stack)
# input_stack = [test1, test2, test3]



print(input_stack)
sample_instruction = {1: {"count": 1, "from": 2, "to": 1}}
instructions = {}

with open(_file, encoding='utf-8') as _f:
    for num, line in enumerate(_f):
        instructions.update({num: {"count": int(line.split()[1]), "from": int(line.split()[3]), "to": int(line.split()[5].rstrip('\n'))}})

for num, values in instructions.items():
    from_stack = values["from"]-1
    to_stack = values["to"]-1
    count = values["count"]
    print(f"Moving {count} from {from_stack} to {to_stack}")
    # for i in range(1, count+1):
        # input_stack[to_stack].insert(0, input_stack[from_stack].pop(0))
    input_stack[to_stack] = input_stack[from_stack][:count] + input_stack[to_stack]
    input_stack[from_stack] = input_stack[from_stack][count:]
    print(input_stack)

print(''.join(i[0] for i in input_stack))
