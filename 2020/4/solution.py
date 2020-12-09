from input_utils import *
import re

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
EYE_COLOURS = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])


def solve_1():
    passports = read_input()
    count = 0
    for passport in passports:
        if (all(key in passport.keys() for key in REQUIRED_KEYS)):
            count += 1
    return count


def read_input():
    clean_text = open(get_input_file_name(1), 'r').read().replace('\n', ' ').replace('  ', '\n')
    return [passport_str_to_dict(passport_str) for passport_str in clean_text.splitlines()]


def passport_str_to_dict(passport_str):
    return {entry.split(':')[0]: entry.split(':')[1] for entry in passport_str.split(' ')}


def solve_2():
    passports = read_input()
    count = 0
    for passport in passports:
        try:
            byr = passport['byr']
            iyr = passport['iyr']
            eyr = passport['eyr']
            hgt = passport['hgt']
            hcl = passport['hcl']
            ecl = passport['ecl']
            pid = passport['pid']
            valid = validate_year(byr, 1920, 2002) and validate_year(iyr, 2010, 2020) and validate_year(eyr, 2020, 2030) and validate_height(
                hgt) and validate_hair(hcl) and validate_eyes(ecl) and validate_passport_id(pid)
            if (valid):
                count += 1
        except KeyError:
            continue
    return count


def validate_year(year, maximum, minimum):
    return int(year) >= maximum and int(year) <= minimum


def validate_height(height):
    if (height.endswith('cm')):
        height = int(height.replace('cm', ''))
        return height >= 150 and height <= 193
    elif (height.endswith('in')):
        height = int(height.replace('in', ''))
        return height >= 59 and height <= 76
    else:
        return False


def validate_hair(hair_colour):
    return bool(re.fullmatch("^#[a-f,0-9]{6}$", hair_colour))


def validate_eyes(eye_colour):
    return eye_colour in EYE_COLOURS


def validate_passport_id(passport_id):
    return bool(re.fullmatch("^[0-9]{9}$", passport_id))


print('Part 1')
print(f"Answer: {solve_1()}")

print('Part 2')
print(f"Answer: {solve_2()}")
