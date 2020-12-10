from input_utils import *

def solve_1(data):
    boot_code = list(map(parse_boot_code_entry, data))
    return run_boot_code(boot_code)[0]

def parse_boot_code_entry(boot_code_text):
    split_text = boot_code_text.split(' ')
    return [split_text[0], int(split_text[1])]

def run_boot_code(boot_code):
    visited = set()
    prog_counter = 0
    accumulator = 0
    exit_code = 0
    while(prog_counter != len(boot_code)):
        # Error states
        if (prog_counter in visited):
            exit_code = 1
            break
        if (prog_counter >= len(boot_code)):
            exit_code = 2
            break

        # Normal operation
        visited.add(prog_counter)
        instruction = boot_code[prog_counter][0]
        argument = boot_code[prog_counter][1]
        if (instruction == 'acc'):
            accumulator += argument
            prog_counter += 1
        elif (instruction == 'nop'):
            prog_counter += 1
        elif (instruction == 'jmp'):
            prog_counter += argument

    return (accumulator, exit_code)

def solve_2(data):
    boot_code = list(map(parse_boot_code_entry, data))
    for i in range(len(boot_code)):
        instruction = boot_code[i][0]
        if (instruction == 'acc'):
            continue
        elif (instruction == 'jmp'):
            boot_code[i][0] = 'nop'
        elif (instruction == 'nop'):
            boot_code[i][0] = 'jmp'
        result = run_boot_code(boot_code)
        if (result[1] == 0):
            return result[0]
        else:
            boot_code[i][0] = instruction
    return -404

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")