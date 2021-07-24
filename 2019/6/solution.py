from input_utils import *
from int_code_computer import run_program


def solve_1(data):
    run_program(data, 0)

print('Part 1')
print(f"Answer: {solve_1(get_single_csv_input_as_ints(1))}")