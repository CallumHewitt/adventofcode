from input_utils import *
from solution_utils import *
from operator import *

def solve_list(data):
    sampleSolver=lambda x: solve(x, False)
    return map(sampleSolver, data)

def solve(data, computer_is_broken):
    print("Solving...")
    program = preprocess_program(data, computer_is_broken)
    print(f'{program}')
    index = 0
    while(program[index] != 99):
        program = handle_command(index, program)
        index += 4
    return program

def preprocess_program(data, computer_is_broken):
    program = convert_strings_to_ints(split_csv(data))
    if (computer_is_broken):
        program[1]=12
        program[2]=2
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
    arg1_index = program[index + 1]
    arg2_index = program[index + 2]
    arg1 = program[arg1_index]
    arg2 = program[arg2_index]
    result = function(arg1, arg2)
    result_index = program[index + 3]
    program[result_index] = result
    print(f'{function.__name__}: {index + 1}, {index + 2} into {index + 3}. ({function.__name__}({arg1},{arg2}) = {result})')
    return program

def end(index, program):
    print(f'Something is wrong. End opcode hit at index: {index}.')
    print(f'Program state is: {program}')
    return program

print('Samples:')
for solution in solve_list(get_samples_as_list(1)):
    print(f'Result is: {solution}')

print('Full problem:')
print(f'Result is: {solve(get_input(1), True)}')