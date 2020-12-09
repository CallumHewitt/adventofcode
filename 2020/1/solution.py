from input_utils import *

TARGET=2020

def solve_1(expenses, target=TARGET):
    value_by_subtracted = {}
    for i in expenses:
        value_by_subtracted[target - i] = i
    for i in expenses:
        if (i in value_by_subtracted):
            return (i, value_by_subtracted[i])
    return None

def solve_2(expenses):
    pairs_to_subtracted_by_subtracted = {}
    for i in expenses:
        pairs_to_subtracted_by_subtracted[i] = solve_1(expenses, TARGET - i)
    for key, value in pairs_to_subtracted_by_subtracted.items():
        if (value != None):
            return (key, value[0], value[1])
    return None

print('Part 1')
pair = solve_1(get_input_as_ints(1))
print(f'Pair: {pair}')
print(f'Answer: {pair[0] * pair[1]}')

print('Part 2')
triple = solve_2(get_input_as_ints(1))
print(f'Triple: {triple}')
print(f'Answer: {triple[0] * triple[1] * triple[2]}')