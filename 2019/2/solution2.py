from input_utils import *
from solution_utils import *
from operator import *

target=19690720
max_input=100

def solve(data):
    print("Solving...")
    program = convert_strings_to_ints(split_csv(data))
    solution = 0
    for noun, verb in noun_verb_pairs(max_input):
        prepared_program = list(program)
        prepared_program = apply_inputs(prepared_program, noun, verb)
        run_program(prepared_program)
        if (prepared_program[0] == target):
            print(f'Solution is: noun: {noun}, verb: {verb}')
            break
        else:
            print(f'noun: {noun}, verb: {verb} = {prepared_program[0]}')

def noun_verb_pairs(size):
    for noun in range(size):
        for verb in range(size):
            yield noun, verb

def run_program(program):
    index = 0
    while(program[index] != 99):
        program = handle_command(index, program)
        index += 4
        if (program == None or index >= len(program)):
            break
    return program

def apply_inputs(program, noun, verb):
    program[1]=noun
    program[2]=verb
    return program

def handle_command(index, program):
    switch = {
        1: handle_add,
        2: handle_multiply,
        99: end
    }
    func = switch.get(program[index])
    return func(index, program)

def handle_add(index, program):
    return handle_function(index, program, add)

def handle_multiply(index, program):
    return handle_function(index, program, mul)

def handle_function(index, program, function):
    if ((index + 3) >= len(program)):
        return None
    arg1_index = program[index + 1]
    arg2_index = program[index + 2]
    result_index = program[index + 3]
    if ((arg1_index) >= len(program) or (arg2_index) >= len(program) or (result_index) >= len(program)):
        return None
    arg1 = program[arg1_index]
    arg2 = program[arg2_index]
    result = function(arg1, arg2)
    program[result_index] = result
    # print(f'{function.__name__}: {index + 1}, {index + 2} into {index + 3}. ({function.__name__}({arg1},{arg2}) = {result})')
    return program

def end(index, program):
    print(f'Something is wrong. End opcode hit at index: {index}.')
    print(f'Program state is: {program}')
    return program

solve(get_input(1))