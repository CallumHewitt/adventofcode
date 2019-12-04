from solution_utils import *
from input_utils import *
from typing import Callable
from collections import OrderedDict
import re

def solve_list(data):
    return map(solve, [data[x:x+2] for x in range(0, len(data), 2)])

def solve(data):
    print('Solving...')
    lengths_by_point_1 = create_lengths_by_point_for_bearings(data[0])
    lengths_by_point_2 = create_lengths_by_point_for_bearings(data[1])
    overlapping = find_overlapping_points(lengths_by_point_1.keys(), lengths_by_point_2.keys())
    distances = map_to_wire_length(overlapping, lengths_by_point_1, lengths_by_point_2)
    return min(distances)

def map_to_wire_length(overlapping: Iterable[Point], points1: OrderedDict, points2: OrderedDict):    
    return list(map(lambda point: points1.get(point) + points2.get(point), overlapping))

def create_lengths_by_point_for_bearings(bearings):
    points = OrderedDict()
    points[Point(0,0)] = 0
    split_regex = re.compile('([a-zA-Z])([0-9]+)')
    for bearing in bearings:
        direction_distance = split_regex.match(bearing)
        points = add_points(points, direction_distance.group(1), int(direction_distance.group(2)))
    del points[Point(0,0)]
    return points

def add_points(points: OrderedDict, direction: str, line_length: int):
    result = []
    current_point = next(reversed(points))
    if (direction == 'R'):
        for x in range(1, line_length + 1):
            points[Point(current_point.x + x, current_point.y)] = points.get(current_point) + x
    elif (direction == 'L'):
        for x in range(1, line_length + 1):
            points[Point(current_point.x - x, current_point.y)] = points.get(current_point) + x
    elif (direction == 'U'):
        for y in range(1, line_length + 1):
            points[Point(current_point.x, current_point.y + y)] = points.get(current_point) + y
    elif (direction == 'D'):
        for y in range(1, line_length + 1):
            points[Point(current_point.x, current_point.y - y)] = points.get(current_point) + y
    return points

def find_overlapping_points(points1, points2):
    points1_set = set(points1)
    points2_set = set(points2)
    return points1_set.intersection(points2_set)

print('Samples:')
for solution in solve_list(get_sample_as_csv_lists(1)):
    print(f'Result is: {solution}')

print('Full problem:')
print(f'Result is: {solve(get_input_as_csv_lists(1))}')