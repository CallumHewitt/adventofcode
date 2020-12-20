from input_utils import *
import math
import re


def solve_1(data):
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = {}
    for line in data:
        if (line[0:4] == 'mask'):
            current_mask = line[7:]
        else:
            address_value = extract_address_value(line)
            address = address_value[0]
            value = apply_mask_overwrite(address_value[1], current_mask)
            memory[address] = value
    return sum(memory.values())


def extract_address_value(line):
    data_search = re.search("mem\[(\d*)\] = (\d*)", line)
    if (data_search):
        return (int(data_search.group(1)), int(data_search.group(2)))
    else:
        raise ValueError(f'Unparsable mem line: {line}')


def apply_mask_overwrite(number, mask):
    for i in range(0, 36):
        if (mask[i] != 'X'):
            number = update_bit(number, 35 - i, int(mask[i]))
    return number


def update_bit(number, bit_index, new_bit):
    if (new_bit == 1):
        return number | (1 << bit_index)
    elif (new_bit == 0):
        return number & ~(1 << bit_index)
    else:
        raise ValueError('new_bit must be 1 or 0')


def solve_2(data):
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = {}
    for line in data:
        if (line[0:4] == 'mask'):
            current_mask = line[7:]
        else:
            address_value = extract_address_value(line)
            addresses = find_memory_addresses(address_value[0], current_mask)
            for address in addresses:
                memory[address] = address_value[1]
    return sum(memory.values())

def find_memory_addresses(start_address, mask):
    mask = list(mask)
    for i in range(len(mask)):
        if (get_bit(start_address, 35 - i) == 1 and mask[i] == '0'):
            mask[i] = '1'
    return get_complete_addresses(''.join(mask))

def get_bit(number, bit_index):
    return (number >> bit_index) & 1

def get_complete_addresses(mask):
    if len(mask) == 1:
        if (mask[0] == 'X'):
            return ['1', '0']
        else:
            return [mask]
    elif mask[0] == 'X':
        masks = map(lambda m: ['1' + m, '0' + m], get_complete_addresses(mask[1:]))
        return [mask for sublist in masks for mask in sublist]        
    else:
        return list(map(lambda m: mask[0] + m, get_complete_addresses(mask[1:])))

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")