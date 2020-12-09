from input_utils import *

import functools
import re

TARGET_BAG = 'shinygold'


def solve_1(data):
    graph = construct_graph(data)
    outer_bags = set()
    for key in graph:
        if (check_bag(graph, key)):
            outer_bags.add(key)
    return len(outer_bags)


def construct_graph(instructions):
    graph = {}
    for instruction in instructions:
        root, bags = parse_instruction(instruction)
        graph[root] = bags
    return graph


def parse_instruction(instruction):
    clean_instruction = instruction.replace(' ', '').lower()
    root, bags_text = clean_instruction.split('bagscontain')
    bags = [] if 'noother' in bags_text else list(
        map(parse_numbered_bag, bags_text.replace('bags', '').replace('bag', '').replace('.', '').split(',')))
    return [root, bags]


def parse_numbered_bag(numbered_bag_text):
    return re.search(r"([0-9]*)(.*)", numbered_bag_text).groups()


def check_bag(graph, key):
    bag_list = list(map(lambda x: x[1], graph[key]))
    if (not bag_list):
        return False
    if (TARGET_BAG in bag_list):
        return True
    return functools.reduce(lambda a, b: a or b, map(lambda bag: check_bag(graph, bag), bag_list))


def solve_2(data):
    graph = construct_graph(data)
    return count_bags(TARGET_BAG, graph) - 1


def count_bags(bag, graph):
    bag_list_with_numbers = graph[bag]
    if (not bag_list_with_numbers):
        return 1
    else:
        bag_counts = map(lambda bag_with_num: int(bag_with_num[0]) * count_bags(bag_with_num[1], graph), bag_list_with_numbers)
        return 1 + functools.reduce(lambda a, b: a + b, bag_counts)


print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")
