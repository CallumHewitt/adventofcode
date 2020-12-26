from typing import OrderedDict
from input_utils import *
from functools import reduce
import math
import copy

import re

ON = '.'
OFF = '#'

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

NO_FLIP = 'x'
V_FLIPPED = 'v'
H_FLIPPED = 'h'

def solve_1(data):
    tiles_by_id = dict(map(parse_input, data.split("\n\n")))
    borders_by_id = dict(map(lambda item: ((item[0], NO_FLIP, 0), get_borders(item[1])), tiles_by_id.items()))#
    borders_by_id_flip_h = flip_borders_h(borders_by_id)
    borders_by_id_flip_v = flip_borders_v(borders_by_id)
    combined_borders = borders_by_id | borders_by_id_flip_h
    combined_borders = combined_borders | borders_by_id_flip_v
    encoded_borders_by_id = encode_all_borders(combined_borders)
    border_counts = count_matching_borders(encoded_borders_by_id)
    for key, counts in border_counts.items():
        print(f'{key}: {counts}')
    potential_corners = find_potential_corners(border_counts)
    print(f'Corners multiplier: {reduce(lambda a, b: a*b, set(map(lambda c: int(c[0]), potential_corners)), 1)}')
    produce_table(border_counts, encoded_borders_by_id, potential_corners)
    return None

def parse_input(tile_input):
    search = re.search("Tile (\d*):\n(.*)", tile_input, re.DOTALL)
    return (search.group(1), search.group(2).split("\n"))

def get_borders(tile):
    borders = {
       UP: tile[0],
       DOWN: tile[-1],
       LEFT: ''.join([row[0] for row in tile]),
       RIGHT: ''.join([row[-1] for row in tile])
    }
    return borders

def flip_borders_h(borders_by_id):
    x_borders = {}
    for id, border in borders_by_id.items():
        x_borders[(id[0], H_FLIPPED, id[2])] = {
            UP: reverse_str(border[UP]),
            DOWN: reverse_str(border[DOWN]),
            RIGHT: border[LEFT],
            LEFT: border[RIGHT]
        }
    return x_borders

def flip_borders_v(borders_by_id):
    y_borders = {}
    for id, border in borders_by_id.items():
        y_borders[(id[0], V_FLIPPED, id[2])] = {
            DOWN: border[UP],
            UP: border[DOWN],
            LEFT: reverse_str(border[LEFT]),
            RIGHT: reverse_str(border[RIGHT]),
        }
    return y_borders

def reverse_str(str):
    return ''.join(reversed(str))

def encode_all_borders(borders_by_id):
    encoded_borders = {}
    for id, borders in borders_by_id.items():
        encoded_borders[id] = dict(map(lambda item: (item[0], encode_border(item[1])), borders.items()))
    return encoded_borders

def encode_border(border):
    return int(border.replace(ON, '1').replace(OFF, '0'), 2)

def count_matching_borders(borders_by_id):
    counts_by_id = {}
    for id, borders in borders_by_id.items():
        counts_by_id[id] = { UP: 0, DOWN: 0, LEFT: 0, RIGHT: 0 }
        for other_id, other_borders in borders_by_id.items():
            if (id[0] != other_id[0]):
                for direction, value in borders.items():
                    if value in other_borders.values():
                        counts_by_id[id][direction] += 1
    return counts_by_id

def find_potential_corners(border_counts):
    corners = []
    for id, border_count in border_counts.items():
        potential_corner = sum(1 for i in border_count.values() if i > 0) == 2
        if (potential_corner):
            corners.append(id)
    return corners

def produce_table(border_counts, borders_by_id, potential_corners):
    side_size = int(math.sqrt(len(border_counts)/3))
    open_borders_all = create_open_borders_dict(border_counts, borders_by_id)

    # Try and place each potential corner first to see what will produce a stable image
    for corner in potential_corners:    
        print('Hit')
        open_borders = copy.deepcopy(open_borders_all)
        table = [[None for i in range(side_size)] for j in range(side_size)]
    
        first_borders = open_borders[corner]
        first_y = 0 if UP in first_borders else side_size - 1 # Has a top border, sits at bottom
        first_x = 0 if RIGHT in first_borders else side_size - 1 # Has a right border, sits on left
        table[first_y][first_x] = corner
        print(table[first_y][first_x])
        open_borders = remove_conflicting_from_open_borders(corner, open_borders)

        for y in range(side_size):
            for x in range(side_size):
                if ([table[y][x]] == None):
                    continue
                full_id = table[y][x]
                print(full_id)
                for side, border_number in open_borders[full_id].items():
                    print(side, border_number)


        

    exit()
    
    for item in open_borders.items():
        print(item)

    first_corner = corners[0]
    first_borders = open_borders[first_corner]
    open_borders = remove_matching_short_id_from_open_borders(first_corner, open_borders)
    
    first_y = 0 if first_borders[0] == -1 else side_size - 1 # At top 
    first_x = 0 if first_borders[2] == -1 else side_size - 1 # On right
    table[first_y][first_x] = (first_corner, 0)
    placed_count = 1

    target = int(len(border_counts) / 3)
    print(f'Placed corner: {first_corner} at {(first_x,first_y)}')
    while(placed_count < target):
        for y in range(side_size):
            for x in range(side_size):
                cell_id = table[y][x][0]
                if (cell_id in open_borders):
                    borders = open_borders[cell_id]
                    print(f'Cell {cell_id} {(x,y)}: {borders}')
                    if borders[0] != -1:
                        print(f'Searching bottom for top')
                        candidate = find_candidate(1, cell_id, borders[0], open_borders)
                        open_borders = remove_matching_short_id_from_open_borders(candidate[0], open_borders)
                        open_borders[candidate[0]] = rotate_borders(open_borders[candidate[0]], candidate[1])
                        table[y-1][x] = candidate
                        placed_count += 1
                        print(f'Added {candidate} in {(x,y-1)}')
                        borders[0] = -1
                        open_borders[candidate[0]][1] = -1
                        print(f'Closed cell top and bottom border')
                    elif borders[1] != -1:
                        print(f'Searching top for bottom')
                        candidate = find_candidate(0, cell_id, borders[1], open_borders)
                        open_borders = remove_matching_short_id_from_open_borders(candidate[0], open_borders)
                        open_borders[candidate[0]] = rotate_borders(open_borders[candidate[0]], candidate[1])
                        table[y+1][x] = candidate
                        placed_count += 1
                        print(f'Added {candidate} in {(x,y+1)}')
                        borders[1] = -1
                        open_borders[candidate[0]][0] = -1
                        print(f'Closed cell bottom and top border')
                    elif borders[2] != -1:
                        print(f'Searching right for left')
                        candidate = find_candidate(3, cell_id, borders[2], open_borders)
                        open_borders = remove_matching_short_id_from_open_borders(candidate[0], open_borders)
                        open_borders[candidate[0]] = rotate_borders(open_borders[candidate[0]], candidate[1])
                        table[y][x-1] = candidate
                        placed_count += 1
                        print(f'Added {candidate} in {(x-1,y)}')
                        borders[2] = -1
                        open_borders[candidate[0]][3] = -1
                        print(f'Closed cell left and right border')
                    elif borders[3] != -1:
                        print(f'Searching left for right')
                        candidate = find_candidate(2, cell_id, borders[3], open_borders)
                        open_borders = remove_matching_short_id_from_open_borders(candidate[0], open_borders)
                        open_borders[candidate[0]] = rotate_borders(open_borders[candidate[0]], candidate[1])
                        table[y][x+1] = candidate
                        placed_count += 1
                        print(f'Added {candidate} in {(x+1,y)}')
                        borders[3] = -1
                        open_borders[candidate[0]][2] = -1
                        print(f'Closed cell right and left border')
    return table
   

def create_open_borders_dict(border_counts, border_by_id):
    open_borders = {}
    for id, border_count in border_counts.items():
        open_borders[id] = {}
        for border, count in border_count.items():            
            if count:
                open_borders[id][border] = border_by_id[id][border]
    return open_borders


def remove_conflicting_from_open_borders(selected_full_id, open_borders):
    return dict(filter(lambda item: not (item[0][0] == selected_full_id[0] and item[0] != selected_full_id), open_borders.items()))


def add_tile(side_to_add, side_of_added, border, cell_id, open_borders, table):
    candidate = find_candidate(side_of_added, cell_id, border, open_borders)
    open_borders = remove_matching_short_id_from_open_borders(candidate[0], open_borders)
    open_borders[candidate[0]] = rotate_borders(open_borders[candidate[0]], candidate[1])
    table[y][x+1] = candidate
    print(f'Added {candidate} in {(x+1,y)}')
    open_borders[cell_id][side_to_add] = -1
    open_borders[candidate[0]][2] = -1

def find_candidate(side, pair_id, border, open_borders):
    # 0 top, 1 bottom, 2 left, 3 right
    for i in range(4): # Check each rotation
        for id, borders in open_borders.items():
            rotated_borders = rotate_borders(borders, 90 * i)
            if (rotated_borders[side] == border and id != pair_id):
                return (id, 90 * i)
    raise ValueError('No suitable candidate for side {} for border {}')

def rotate_borders(borders, rotation):
    # 0 top, 1 bottom, 2 left, 3 right
    if rotation == 0:
        return borders
    elif rotation == 90:
        return [borders[2], borders[3], borders[1], borders[0]]
    elif rotation == 180:
        return [borders[1], borders[0], borders[3], borders[2]]
    elif rotation == 270:
        return [borders[3], borders[2], borders[0], borders[1]]


    
    



print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")
