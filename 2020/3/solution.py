from input_utils import *
import functools

RIGHT_STEPS = 3
DOWN_STEPS = 1
SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

# Misread problem - Decided to keep this here due to effort
def solve_1_wrong(data):
    WIDTH = len(data[0])
    current_x = 0
    current_y = 0
    trees_hit = 0
    while(current_y < len(data)):
        x_trees = data[current_y][current_x + 1: current_x + 1 + RIGHT_STEPS]
        current_x = (current_x + RIGHT_STEPS) % WIDTH
        y_trees = []
        if (current_y != len(data) - 1):
            y_trees = list(map(lambda i: data[i][current_x], range(current_y + 1, current_y + 1 + DOWN_STEPS)))
        current_y = current_y + DOWN_STEPS
        def hit_tree_predicate(x): return 1 if x == '#' else 0
        trees_hit += sum(map(hit_tree_predicate, x_trees)) + sum(map(hit_tree_predicate, y_trees))
    return trees_hit


def solve_1(data, right_steps=RIGHT_STEPS, down_steps=DOWN_STEPS):
    WIDTH = len(data[0])
    current_x = 0
    current_y = 0
    trees_hit = 0
    while(current_y < len(data)):
        current_x = (current_x + right_steps) % WIDTH
        current_y = current_y + down_steps
        print(f'{current_x}, {current_y}')
        if (current_y < len(data) and data[current_y][current_x] == '#'):
            trees_hit += 1
    return trees_hit


def solve_2(data):
    return functools.reduce(lambda a, b: a*b, map(lambda slope: solve_1(data, slope[0], slope[1]), SLOPES))


print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list(1))}")
