import operator
from typing import List


class Command:

    def __init__(self, op_code: int, param_mode: str):
        self.op_code = op_code
        self.param_mode = param_mode


def run_program(program: List[int], output_position: int, noun=None, verb=None):
    update_program(program, noun, verb)
    prog_counter = 0
    command = parse_command(program[prog_counter])
    while (command.op_code != 99):
        op_code = command.op_code
        if (op_code == 1):
            # Add
            operate_and_save(program, prog_counter, command.param_mode, operator.add)
            prog_counter += 4
        elif (op_code == 2):
            # Multiply
            operate_and_save(program, prog_counter, command.param_mode, operator.mul)
            prog_counter += 4
        elif (op_code == 3):
            # Input
            save_input(program, prog_counter)
            prog_counter += 2
        elif (op_code == 4):
            # Output
            print_output(program, prog_counter)
            prog_counter += 2
        elif (op_code == 5):
            prog_counter = calculate_new_prog_counter(program, prog_counter, command.param_mode, False)
        elif (op_code == 6):
            prog_counter = calculate_new_prog_counter(program, prog_counter, command.param_mode, True)
        elif (op_code == 7):
            boolean_operate_and_save(program, prog_counter, command.param_mode, operator.lt)
            prog_counter += 4
        elif (op_code == 8):
            boolean_operate_and_save(program, prog_counter, command.param_mode, operator.eq)
            prog_counter += 4
        else:
            raise RuntimeError(f'Unknown op_code {op_code} at prog_counter {prog_counter}')

        command = parse_command(program[prog_counter])
    return program[output_position]


def update_program(program: List[int], noun, verb):
    if (noun is not None):
        program[1] = noun
    if (verb is not None):
        program[2] = verb


def parse_command(command_int):
    command_str = "{:05d}".format(command_int)
    return Command(int(command_str[3:]), command_str[0:3])


def operate_and_save(program, prog_counter, param_mode, operation):
    input_1 = program[prog_counter + 1]
    input_2 = program[prog_counter + 2]
    input_3 = program[prog_counter + 3]
    arg_1 = program[input_1] if (int(param_mode[2]) == 0) else input_1
    arg_2 = program[input_2] if (int(param_mode[1]) == 0) else input_2
    value = operation(arg_1, arg_2)
    program[input_3] = value


def save_input(program, prog_counter):
    value = int(input('Input requested: '))
    position = program[prog_counter + 1]
    program[position] = value


def print_output(program, prog_counter):
    position = program[prog_counter + 1]
    print(f'Output: {program[position]}')


def calculate_new_prog_counter(program, prog_counter, param_mode, jumpOnZero):
    input_1 = program[prog_counter + 1]
    input_2 = program[prog_counter + 2]
    arg_1 = program[input_1] if (int(param_mode[2]) == 0) else input_1
    arg_2 = program[input_2] if (int(param_mode[1]) == 0) else input_2
    if ((jumpOnZero and arg_1 == 0) or (not jumpOnZero and arg_1 != 0)):
        return arg_2
    else:
        return prog_counter + 3

def boolean_operate_and_save(program, prog_counter, param_mode, operation):
    input_1 = program[prog_counter + 1]
    input_2 = program[prog_counter + 2]
    input_3 = program[prog_counter + 3]
    arg_1 = program[input_1] if (int(param_mode[2]) == 0) else input_1
    arg_2 = program[input_2] if (int(param_mode[1]) == 0) else input_2
    value = operation(arg_1, arg_2)
    if (value):
        program[input_3] = 1
    else:
        program[input_3] = 0
