from input_utils import *
from string import ascii_lowercase

import functools

def solve_1(data):
    group_answers = list(map(lambda entry: set(list(entry.replace('#',''))), data.replace('\n','#').replace('##', '\n').splitlines()))
    return sum(map(lambda row: len(row), group_answers))

def solve_2(data):
    group_answers_split = list(map(lambda group: group.split('#'), data.replace('\n','#').replace('##', '\n').splitlines()))
    return sum(map(get_count_where_all_picked, group_answers_split))

def get_count_where_all_picked(group_answer_split):
    count_dictionary = {}
    group_answers_combined = ''.join(group_answer_split)
    for char in group_answers_combined:
        if char not in count_dictionary:
            count_dictionary[char] = 0
        count_dictionary[char] += 1
    count = 0
    for value in count_dictionary.values():
        if (value == len(group_answer_split)):
            count += 1
    return count
        

print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input(1))}")