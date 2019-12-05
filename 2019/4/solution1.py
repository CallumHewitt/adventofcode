from solution_utils import *
from input_utils import *
import re

PASSWORD_REGEX = re.compile(r'^(?=\d{6}$)(?=\d*(\d)\1+\d*)1*2*3*4*5*6*7*8*9*$')

def solve(data):
    print('Solving...')
    ranges = str.split(data, '-')
    possible_passwords = find_possible_passwords(int(ranges[0]), int(ranges[1]))
    return len(possible_passwords)

def find_possible_passwords(start_range, end_range):
    passwords = []
    for password in range(start_range, end_range + 1):        
        if (test_valid_password(password)):
            passwords.append(password)
    return passwords


def test_valid_password(password):
    return PASSWORD_REGEX.match(str(password)) != None

print('Test valid_password')

sample_1=111111
sample_2=223450
sample_3=123789
sample_4=345555

print(f'{sample_1}, expected True: {test_valid_password(sample_1)}')
print(f'{sample_2}, expected False: {test_valid_password(sample_2)}')
print(f'{sample_3}, expected False: {test_valid_password(sample_3)}')
print(f'{sample_4}, expected True: {test_valid_password(sample_4)}')

print('Full problem:')
print(f'Result is: {solve(get_input(1))}')