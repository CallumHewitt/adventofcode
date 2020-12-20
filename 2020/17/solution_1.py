from input_utils import *
import copy
import math

ACTIVE = '#'
INACTIVE = '.'

def solve_1(data):
    final_universe = simulate_universe(setup_universe(data), activated_test, deactivated_test, 6)
    return count_universe(final_universe, ACTIVE)

def setup_universe(data):
    universe = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            universe[(x,y,0)] = data[y][x]
    return universe

def activated_test(universe, location):
    count = count_nearby(universe, location, ACTIVE)
    return count == 2 or count == 3

def deactivated_test(universe, location):
    count = count_nearby(universe, location, ACTIVE)
    return count == 3

def count_nearby(universe, location, search):
    count = 0
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            for z_dir in range(-1, 2):
                key = (location[0] + x_dir, location[1] + y_dir, location[2] + z_dir) 
                if (key in universe and key != location and universe[key] == search):
                    count += 1
    return count

def simulate_universe(universe, activated_test, deactivated_test, cycles):
    for i in range(0, cycles):
        universe = grow_universe(universe)
        next_universe = copy.deepcopy(universe)
        for location, state in universe.items():
            if (state == ACTIVE):
                next_universe[location] = ACTIVE if activated_test(universe, location) else INACTIVE
            else:
                next_universe[location] = ACTIVE if deactivated_test(universe, location) else INACTIVE
        universe = next_universe        
    print_universe(universe)
    return universe

def grow_universe(universe):
    new_universe = {}
    for location, state in universe.items():
        new_universe[location] = state
        for x_dir in range(-1, 2):
            for y_dir in range(-1, 2):
                for z_dir in range(-1, 2):
                    key = (location[0] + x_dir, location[1] + y_dir, location[2] + z_dir) 
                    if key not in universe:
                        new_universe[key] = INACTIVE
    return new_universe

def print_universe(universe):
    max_x = max(map(lambda key: key[0], universe.keys()))
    max_y = max(map(lambda key: key[1], universe.keys()))
    max_z = max(map(lambda key: key[2], universe.keys()))
    min_x = min(map(lambda key: key[0], universe.keys()))
    min_y = min(map(lambda key: key[1], universe.keys()))
    min_z = min(map(lambda key: key[2], universe.keys()))
    for z in range(min_z, max_z + 1):
        lines = []
        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                line += universe[(x,y,z)]
            lines.append(line)
        print(f'z = {z}')
        print('\n'.join(lines))
        print()

def count_universe(universe, search):
    count = 0
    for value in universe.values():
        if (value == search):
            count += 1
    return count


print('Part 1')
print(f"Answer: {solve_1(get_input_as_list_of_chars(1))}")