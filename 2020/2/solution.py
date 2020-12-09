from input_utils import *

import re

def solve(data, valid_func):
    return sum(valid_func(entry) for entry in data)

def is_valid_1(entry):
    min_count, max_count = entry[0].split('-')
    character = entry[1].replace(':', '')
    password = str(entry[2])

    pattern_str = "^([^" + character + "]*" + character + "[^" + character + "]*){" + min_count + "," + max_count + "}$"
    return bool(re.fullmatch(pattern_str, password))

def is_valid_2(entry):
    pos_1, pos_2 = map(int, entry[0].split('-'))
    pos_1 -= 1
    pos_2 -= 1
    character = entry[1].replace(':', '')
    password = str(entry[2])    

    return (password[pos_1] == character or password[pos_2] == character) and (not (password[pos_1] == character and password[pos_2] == character))
    
    
print('Part 1')
print(f"Answer: {solve(get_input_as_csv_lists(1, ' '), is_valid_1)}")

print('Part 2')
print(f"Answer: {solve(get_input_as_csv_lists(1, ' '), is_valid_2)}")