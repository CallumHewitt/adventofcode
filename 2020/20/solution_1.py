from input_utils import *
import re

ON = '.'
OFF = '#'

def solve_1(data):
    tiles_by_id = dict(map(parse_input, data.split("\n\n")))
    borders_by_id = dict(map(lambda item: (item[0], get_borders(item[1])), tiles_by_id.items()))
    borders_by_id_with_flips = add_flips(borders_by_id)
    encoded_borders_by_id = encode_all_borders(borders_by_id_with_flips)
    print(count_matching_borders(encoded_borders_by_id))

def parse_input(tile_input):
    search = re.search("Tile (\d*):\n(.*)", tile_input, re.DOTALL)
    return (search.group(1), search.group(2).split("\n"))

def get_borders(tile):
    # top, bottom, left, right
    borders = (
       tile[0],
       tile[-1],
       ''.join([row[0] for row in tile]),
       ''.join([row[1] for row in tile]),
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



print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")
