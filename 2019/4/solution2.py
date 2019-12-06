from solution_utils import *
from input_utils import *
import re

# \d*\2{1}\d* doesn't capture the cases where the double character group starts at the first character or the second character.
# Therefore there are three cases wrapped up here. Please let me know if you can see the issue!
PASSWORD_REGEX = re.compile(r'^(?=\d{6}$)((?=\d*(\d)\2{1}\d*)(?!\d*\2{3}\d*)|(?=(\d)\3{1}\d*)(?!\d*\3{3,6}\d*)|(?=\d(\d)\4{1}\d*)(?!\d*\4{3,6}\d*))1*2*3*4*5*6*7*8*9*$')

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

samples = {
    112222: True,
    111122: True,
    112233: True,
    333455: True,
    112222: True,
    122333: True,
    123344: True,
    123445: True,
    123455: True,
    123444: False
}

for sample, expectation in samples.items():
    print(f'{sample}, expected {expectation}: {test_valid_password(sample)}')

print('Full problem:')
print(f'Result is: {solve(get_input(1))}')