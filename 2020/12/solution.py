from input_utils import *
from solution_utils import *

NORTH=(0, 1)
SOUTH=(0, -1)
EAST=(1, 0)
WEST=(-1, 0)

DIRECTIONS=[NORTH, EAST, SOUTH, WEST]

def solve_1(data):
    instructions = list(map(parse_instruction, data))
    x = 0
    y = 0
    direction = EAST
    for instruction in instructions:
        update = step(instruction[0], instruction[1], x, y, direction)
        x = update[0]
        y = update[1]
        direction = update[2]
    return manhattan_distance(0, 0, x, y)

def parse_instruction(instruction):
    return (instruction[0], int(instruction[1:]))

def step(command, distance, x, y, direction):
    if (command == 'N'):
        return (x, y + distance, direction)
    elif (command == 'S'):
        return (x, y - distance, direction)
    elif (command == 'E'):
        return (x + distance, y, direction)
    elif (command == 'W'):
        return (x - distance, y, direction)
    elif (command == 'F'):
        return (x + (direction[0] * distance), y + (direction[1] * distance), direction)
    elif (command == 'L'):
        return (x, y, DIRECTIONS[(DIRECTIONS.index(direction) - int(distance / 90))])
    elif (command == 'R'):
        return (x, y, DIRECTIONS[(DIRECTIONS.index(direction) + int(distance / 90)) % 4])
    else:
        raise ValueError(f'Invalid step requested: {command}')

def solve_2(data):
    instructions = list(map(parse_instruction, data))
    x = 0
    y = 0
    waypoint = (10, 1)
    for instruction in instructions:
        update = step_waypoint(instruction[0], instruction[1], x, y, waypoint)
        x = update[0]
        y = update[1]
        waypoint = update[2]
    return manhattan_distance(0, 0, x, y)

def step_waypoint(command, distance, x, y, waypoint):
    if (command == 'N'):
        return (x, y, (waypoint[0], waypoint[1] + distance))
    elif (command == 'S'):
        return (x, y, (waypoint[0], waypoint[1] - distance))
    elif (command == 'E'):
        return (x, y, (waypoint[0] + distance, waypoint[1]))
    elif (command == 'W'):
        return (x, y, (waypoint[0] - distance, waypoint[1]))
    elif (command == 'F'):
        return (x + (waypoint[0] * distance), y + (waypoint[1] * distance), waypoint)
    elif (command == 'L'):
        angle = distance % 360
        if (angle == 90):
            return (x, y, (-waypoint[1], waypoint[0]))
        if (angle == 180):
            return (x, y, (-waypoint[0], -waypoint[1]))
        if (angle == 270):
            return (x, y, (waypoint[1], -waypoint[0]))
        else:
            return (x, y, waypoint)
    elif (command == 'R'):
        angle = distance % 360
        if (angle == 90):
            return (x, y, (waypoint[1], -waypoint[0]))
        if (angle == 180):
            return (x, y, (-waypoint[0], -waypoint[1]))
        if (angle == 270):
            return (x, y, (-waypoint[1], waypoint[0]))
        else:
            return (x, y, waypoint)
    else:
        raise ValueError(f'Invalid step requested: {command}')

print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")