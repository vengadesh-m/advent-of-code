import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

input_type = os.environ.get("INPUT_TYPE")
sample_file = f"{BASE_DIR}{SEP}sample_inputs{SEP}day01"
actual_file = f"{BASE_DIR}{SEP}actual_inputs{SEP}day01"


def puzzle_input():
    file_name = sample_file if input_type == 'sample' else actual_file
    with open(file_name, 'r') as _f:
        result = _f.readlines()
    return result


