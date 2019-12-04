from solution_utils import *
from input_utils import *
from typing import Callable
import re

def solve_list(data):
    return map(solve, [data[x:x+2] for x in range(0, len(data), 2)])

def solve(data):
    print('Solving...')
    points1 = create_points_for_bearings(data[0])
    points2 = create_points_for_bearings(data[1])
    overlapping = find_overlapping_points(points1, points2)
    distances = map_to_manhattan_distance_from_port(overlapping)
    return min(distances)

def map_to_manhattan_distance_from_port(points: Iterable[Point]):
    to_manhattan: Callable[[Point], int] = lambda p: p.manhattan_distance(Point(0,0))
    return list(map(to_manhattan, points))

def create_points_for_bearings(bearings):
    current_point = Point(0,0)
    points = [Point(0,0)]
    split_regex = re.compile('([a-zA-Z])([0-9]+)')
    for bearing in bearings:
        direction_distance = split_regex.match(bearing)
        points += create_points(current_point, direction_distance.group(1), int(direction_distance.group(2)))
        current_point = points[len(points) - 1]
    return points[1:]

def create_points(current_point: Point, direction: str, distance: int):
    result = []
    if (direction == 'R'):
        result = [Point(current_point.x + x, current_point.y) for x in range(1, distance + 1)]
    elif (direction == 'L'):
        result = [Point(current_point.x - x, current_point.y) for x in range(1, distance + 1)]
    elif (direction == 'U'):
        result = [Point(current_point.x, current_point.y + y) for y in range(1, distance + 1)]
    elif (direction == 'D'):
        result = [Point(current_point.x, current_point.y - y) for y in range(1, distance + 1)]
    return result

def find_overlapping_points(points1, points2):
    points1_set = set(points1)
    points2_set = set(points2)
    return points1_set.intersection(points2_set)



print('Samples:')
for solution in solve_list(get_sample_as_csv_lists(1)):
    print(f'Result is: {solution}')

print('Full problem:')
print(f'Result is: {solve(get_input_as_csv_lists(1))}')