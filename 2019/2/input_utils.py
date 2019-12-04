from typing import Iterable
import functools
import csv

input_1_file_name = 'input1.txt'
input_2_file_name = 'input2.txt'

def get_input(input_id: int):
    file_name = get_input_file_name(input_id)
    print('Getting input as string from ' + file_name)
    return read_file_as_string(file_name)

def get_input_file_name(input_id: int):
    return input_1_file_name if input_id == 1 else input_2_file_name

def read_file_as_string(file_name: str):
    return open(file_name, 'r').read()

def get_input_as_list(input_id: int):
    file_name = get_input_file_name(input_id)
    print('Getting input as list from ' + file_name)
    return read_file_as_list(file_name)

def read_file_as_list(file_name: str):
    return open(file_name, 'r').readlines()

sample_1_file_name = 'samples1.txt'
sample_2_file_name = 'samples2.txt'

def get_samples_as_list(sample_num: int):
    file_name = get_sample_file_name(sample_num)
    print('Getting samples as list from ' + file_name)
    return read_file_as_list(file_name)

def get_sample_file_name(sample_id: int):
    return sample_1_file_name if sample_id == 1 else sample_2_file_name

def split_csv(csv: str):
    return list(map(str.strip, csv.split(',')))

def split_csv_list(csv: Iterable[str], delimiter=','):
    return list(csv.reader(csv), skipinitialspace=False, delimiter=delimiter)

def convert_strings_to_ints(strings: Iterable[str]):
    return list(map(int, strings))