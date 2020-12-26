from input_utils import *
import re

# Hex stored in 'virtual' 2D array. Actual storage is a dict with key of (x,y) tuple to avoid storing unnecessary data
# and avoid having to grow the array as more tiles are added. Only black tiles are included in the dict.
#
# [ X H X H X ]
# [ H X H X H ]
# [ X H X H X ]
#
# ( H == Valid Hex Position, X == Invalid Hex Position)
#
# East is +2 on X
# West is -2 on X
# South East is +1 on X, -1 on Y
# South West is -1 on X, -1 on Y
# North East is +1 on X, +1 on Y
# North West is -1 on X, +1 on Y
#

BLACK = 1

EAST = (2, 0)
WEST = (-2, 0)
NORTH_EAST = (1, 1)
NORTH_WEST = (-1, 1)
SOUTH_EAST = (1, -1)
SOUTH_WEST = (-1, -1)

DIRECTIONS = [EAST, WEST, NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST]


def solve(data, days):
    instructions = list(map(parse_instruction, data))
    tiles = process_instructions(instructions)
    print(f'Black tiles on init: {count_tiles(tiles, BLACK)}')
    for i in range(days):
        new_tiles = {}
        for position in tiles.keys():
            count = count_adjacent(tiles, position)
            if (not(count == 0 or count > 2)):
                new_tiles[position] = BLACK
            adjacent_positions = get_adjacent_positions(position)
            for adj_position in adjacent_positions:
                if (count_adjacent(tiles, adj_position) == 2):
                    new_tiles[adj_position] = BLACK
        tiles = new_tiles
    print(f'Black tiles after {days}: {count_tiles(tiles, BLACK)}')


def parse_instruction(input):
    groups = re.findall("([sn]?[ew]{1})", input)
    return list(map(input_step_to_direction, groups))


def input_step_to_direction(step):
    if (step == 'e'):
        return EAST
    if (step == 'w'):
        return WEST
    if (step == 'ne'):
        return NORTH_EAST
    if (step == 'nw'):
        return NORTH_WEST
    if (step == 'se'):
        return SOUTH_EAST
    if (step == 'sw'):
        return SOUTH_WEST


def process_instructions(instructions):
    tiles = {}
    for instruction in instructions:
        position = [0, 0]
        for step in instruction:
            position[0] += step[0]
            position[1] += step[1]
        position = tuple(position)
        if (position not in tiles):
            tiles[position] = BLACK
        else:
            del tiles[position]
    return tiles


def count_tiles(tiles, colour):
    return sum([value for value in tiles.values() if value == colour])


def count_adjacent(tiles, position):
    count = 0
    for direction in DIRECTIONS:
        if (direction[0] + position[0], direction[1] + position[1]) in tiles:
            count += 1
    return count


def get_adjacent_positions(position):
    adjacents = []
    for direction in DIRECTIONS:
        adjacents.append(
            (direction[0] + position[0], direction[1] + position[1]))
    return adjacents


solve(get_input_as_list(1), 100)
