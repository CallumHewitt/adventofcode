from os import P_NOWAITO
from input_utils import *
from functools import reduce

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
    return reduce(lambda a, b: a*b, map(int, potential_corners), 1)

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
        counts_by_id[id]= dict(map(lambda border: (border, 0), borders))
        for other_id, other_borders in borders_by_id.items():
            if (id[0:-1] != other_id[0:-1]):
                for border in borders:
                    if border in other_borders:
                        counts_by_id[id][border] += 1
    return counts_by_id

def find_potential_corners(border_counts):
    corners = set()
    for id, border_count in border_counts.items():
        potential_corner = sum(1 for i in border_count.values() if i > 0) == 2
        if (potential_corner):
            corners.add(id[:-1])
        print(f"{id}: {border_count} {'*' if potential_corner else ''}")
    return corners


print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")
