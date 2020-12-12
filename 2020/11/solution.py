from input_utils import *
import copy

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def solve_1(seats):
    processed_seats = process_seats(seats, count_nearby, 4)
    return count_total_seats(processed_seats, OCCUPIED)

def solve_2(seats):
    processed_seats = process_seats(seats, count_visible, 5)
    return count_total_seats(processed_seats, OCCUPIED)

def process_seats(seats, count_func, occupation_threshold):
    change_made = True
    while change_made:
        next_seats = copy.deepcopy(seats)
        change_made = False
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == EMPTY and count_func(seats, x, y, OCCUPIED) == 0:
                    next_seats[y][x] = OCCUPIED
                    change_made = True
                elif seats[y][x] == OCCUPIED and count_func(seats, x, y, OCCUPIED) >= occupation_threshold:
                    next_seats[y][x] = EMPTY
                    change_made = True
        seats = next_seats
    return seats


def count_nearby(seats, x, y, search):
    count = 0
    max_x = len(seats[y])
    max_y = len(seats)
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            if (x_dir == 0 and y_dir == 0) or (x + x_dir >= max_x) or (y + y_dir >= max_y) or (x + x_dir < 0) or (y + y_dir < 0):
                continue
            else:
                if seats[y+y_dir][x+x_dir] == search:
                    count += 1
    return count


def count_visible(seats, x, y, search):
    count = 0
    max_x = len(seats[y])
    max_y = len(seats)
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            distance_x = x_dir
            distance_y = y_dir
            x_pos = x + distance_x
            y_pos = y + distance_y
            while ((not(x_dir == 0 and y_dir == 0)) and x_pos >= 0 and y_pos >= 0 and x_pos < max_x and y_pos < max_y and seats[y][x] != FLOOR):
                if (seats[y_pos][x_pos] == search):
                    count += 1
                    break
                elif (seats[y_pos][x_pos] != FLOOR):
                    break
                x_pos += x_dir
                y_pos += y_dir            
    return count


def count_total_seats(seats, search):
    count = 0
    for y in range(len(seats)):
        for seat in seats[y]:
            if (seat == search):
                count += 1
    return count


print('Part 1')
print(f"Answer: {solve_1(get_input_as_list_of_chars(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_list_of_chars(1))}")