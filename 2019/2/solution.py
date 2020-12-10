from input_utils import *
from int_code_computer import run_program


def solve_1(data):
    return run_program(data, 0, 12, 2)


def solve_2(data):
    for i in range(100):
        for j in range(100):
            original_data = data[:]
            try:
                result = run_program(data, 0, i, j)
                if (result == 19690720):
                    return i * 100 + j
            except RuntimeError:
                print(f'Failed with ({i}, {j})')
            finally:
                data = original_data[:]
    return -404


print('Part 1')
print(f"Answer: {solve_1(get_single_csv_input_as_ints(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_single_csv_input_as_ints(1))}")
