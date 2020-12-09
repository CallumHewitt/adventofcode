from input_utils import *

import math


def solve_1(data):
    seat_locations = map(convert_binary_code_to_seat_location, data)
    seat_ids = map(convert_seat_location_to_id, seat_locations)
    return max(seat_ids)


def convert_binary_code_to_seat_location(binary_code):
    front_back = binary_code[:7]
    left_right = binary_code[7:]
    return {'row': process_binary_code(front_back, 0, 127, 'F', 'B'), 'column': process_binary_code(left_right, 0, 7, 'L', 'R')}


def process_binary_code(code, minimum, maximum, before_char, after_char):
    if (len(code) == 0 and minimum == maximum):
        return minimum
    elif (len(code) != 0 and minimum != maximum):
        if (code[0] == before_char):
            return process_binary_code(code[1:], minimum, minimum + math.floor((maximum-minimum)/2), before_char, after_char)
        elif (code[0] == after_char):
            return process_binary_code(code[1:], minimum + math.ceil((maximum-minimum)/2), maximum,  before_char, after_char)
    else:
        raise RuntimeError(f'Code was {code}, minimum was {minimum} and maximum was {maximum}')


def convert_seat_location_to_id(location):
    return location['row'] * 8 + location['column']


def solve_2(data):
    seat_locations = map(convert_binary_code_to_seat_location, data)
    seat_ids = list(map(convert_seat_location_to_id, seat_locations))
    seat_ids.sort()
    for i in range(1, len(seat_ids) - 1):
        if (seat_ids[i] - seat_ids[i - 1] > 1):
            return seat_ids[i] - 1
    return -404

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")
