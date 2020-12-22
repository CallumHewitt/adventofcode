from typing import OrderedDict
from input_utils import *
from functools import reduce
import math

import re

ON = '.'
OFF = '#'

def solve_1(data):
    tiles_by_id = dict(map(parse_input, data.split("\n\n")))
    borders_by_id = dict(map(lambda item: (item[0], get_borders(item[1])), tiles_by_id.items()))
    borders_by_id_with_flips = add_flips(borders_by_id)
    encoded_borders_by_id = encode_all_borders(borders_by_id_with_flips)
    border_counts = count_matching_borders(encoded_borders_by_id)
    potential_corners = find_potential_corners(border_counts)
    print(f'Corners multiplier: {reduce(lambda a, b: a*b, map(int, potential_corners), 1)}')
    table = produce_table(border_counts)
    return table

def parse_input(tile_input):
    search = re.search("Tile (\d*):\n(.*)", tile_input, re.DOTALL)
    return (search.group(1), search.group(2).split("\n"))

def get_borders(tile):
    # top, bottom, left, right, top flipped, bottom flipped, left flipped, right flipped
    borders = (
       tile[0],
       tile[-1],
       ''.join([row[0] for row in tile]),
       ''.join([row[-1] for row in tile])
    )
    return borders

def add_flips(borders_by_id):
    with_flips = {}
    for id, borders in borders_by_id.items():
        with_flips[id + 'x'] = borders
        with_flips[id + 'h'] = (reverse_str(borders[0]), reverse_str(borders[1]), borders[3], borders[2])
        with_flips[id + 'v'] = (borders[1], borders[0], reverse_str(borders[2]), reverse_str(borders[3]))
    return with_flips

def reverse_str(str):
    return ''.join(reversed(str))

def encode_all_borders(borders_by_id):
    return dict(map(lambda item: (item[0], list(map(encode_border, item[1]))), borders_by_id.items()))

def encode_border(border):
    return int(border.replace(ON, '1').replace(OFF, '0'), 2)

def count_matching_borders(borders_by_id):
    counts_by_id = {}
    for id, borders in borders_by_id.items():
        counts_by_id[id]= OrderedDict(map(lambda border: (border, 0), borders))
        for other_id, other_borders in borders_by_id.items():
            if (id[0:-1] != other_id[0:-1]):
                for border in borders:
                    if border in other_borders:
                        counts_by_id[id][border] += 1
    return counts_by_id

def find_potential_corners(border_counts, include_variations = False):
    corners = set()
    for id, border_count in border_counts.items():
        potential_corner = sum(1 for i in border_count.values() if i > 0) == 2
        if (potential_corner):
            if (include_variations):
                corners.add(id)
            else:
                corners.add(id[:-1])
    return list(corners)

def produce_table(border_counts):
    side_size = int(math.sqrt(len(border_counts)/3))
    corners = find_potential_corners(border_counts, True)
    table = [[(-1,0) for i in range(side_size)] for j in range(side_size)]

    open_borders = create_open_borders_dict(border_counts)
    
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
   

def create_open_borders_dict(border_counts):
    open_borders = {}
    for id, border_count in border_counts.items():
        open_borders[id] = []
        for border, count in border_count.items():
            if count:
                open_borders[id].append(border)
            else:
                open_borders[id].append(-1)
    return open_borders

def remove_matching_short_id_from_open_borders(id, open_borders):
    return dict(filter(lambda item: item[0] == id or item[0][:-1] != id[:-1], open_borders.items()))

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
