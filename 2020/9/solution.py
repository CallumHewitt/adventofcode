from input_utils import *

PREAMBLE_SIZE = 25

def solve_1(data):
    is_valid = True
    index = PREAMBLE_SIZE;
    while(is_valid):
        is_valid = check_valid(data[index], data[index - PREAMBLE_SIZE:index])
        index += 1
    return data[index - 1]

def check_valid(target, prev_numbers):
    value_by_subtracted = {}
    for number in prev_numbers:
        if ((target - number) != number):
            value_by_subtracted[target - number] = number
    for number in prev_numbers:
        if (number in value_by_subtracted):
            return True
    return False

def solve_2(target, data):
    number_range = get_number_range(target, data)
    number_range.sort()
    return number_range[0] + number_range[-1]

def get_number_range(target, data):
    total = 0
    number_range = []
    for i in range(len(data)):
        total += data[i]
        for j in range(i + 1, len(data)):
            total += data[j]
            number_range.append(data[j])
            if (total == target):
                return number_range
            if (total > target):
                number_range = []
                total = 0
                break


print('Part 1')
part_1_answer = solve_1(get_input_as_ints(1))
print(f"Answer: {part_1_answer}")

print('Part 2')
print(f"Answer: {solve_2(part_1_answer, get_input_as_ints(1))}")