from input_utils import *

def solve_1(data):
    card_public = int(data[0])
    door_public = int(data[1])
    card_loop, door_loop = find_loops(7, card_public, door_public)
    card_encrypted = transform(door_public, card_loop)
    door_encrypted = transform(card_public, door_loop)
    print(f'Verify {card_encrypted} == {door_encrypted}: {card_encrypted == door_encrypted}')
    return card_encrypted

def transform(subject, loop):
    value = 1
    for i in range(loop):
        value = subject * value
        value = value % 20201227
    return value

def find_loops(subject, card_public, door_public):
    card_loop = -1
    door_loop = -1
    loop_size = 1
    value = 1
    while(card_loop == -1 or door_loop == -1):
        value = subject * value
        value = value % 20201227
        if (value == card_public):
            card_loop = loop_size
        elif (value == door_public):
            door_loop = loop_size
        loop_size += 1
    return card_loop, door_loop

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")