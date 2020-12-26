from solution_utils import HashedLinkedList
from input_utils import *


def solve_1(data):
    cups = [int(char) for char in data]
    moved_cups = solve(cups)
    return ''.join(map(str, moved_cups[1:]))


def solve_2(data):
    cups = [int(char) for char in data]
    next = max(cups) + 1
    cups += [i for i in range(next, 1000001)]
    moved_cups = solve(cups, 10000000)
    #print(moved_cups[1], moved_cups[2])
    return moved_cups[1] * moved_cups[2]


def solve(cups, moves=100):
    max_val = len(cups)
    cups = HashedLinkedList(cups, True)
    #print('Initialised cups')
    current_cup = cups.start
    for move in range(1, moves + 1):
        #print(f'\n-- move {move} --')
        #print(f'cups: {cups.to_list()}')
        picked = cups.extract(current_cup.next.value, 3)
        #print(f'pick up: {picked}')
        #print(f'cups after pickup: {cups.to_list()}')
        destination_node = find_destination_node(
            cups, current_cup.value, max_val)
        #print(f'destination: {destination_node.value}')
        cups.reinsert(destination_node.value, picked)
        #print(f'current cup {current_cup}, next cup {current_cup.next}')
        current_cup = current_cup.next
    return cups_from_number(cups.to_list())


def find_destination_node(cups, target, max_val):
    #print(cups.index)
    while True:
        target = (target - 1) % (max_val + 1)
        #print(f'Searching for target: {target}')
        destination_node = cups.get_node(target)
        if (destination_node):
            #print(f'Returning node {destination_node}')
            return destination_node


def cups_from_number(cups, number=1):
    new_cups = []
    index = 0
    while(len(new_cups) < len(cups)):
        if (not new_cups):
            if cups[index] == number:
                new_cups.append(cups[index])
        else:
            new_cups.append(cups[index])
        index = (index + 1) % len(cups)
    return new_cups


print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input(1))}")
