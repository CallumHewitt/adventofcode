from input_utils import *

def solve_1(data):
    current_time = int(data[0])
    buses = list(map(int, filter(lambda x: x != 'x', split_csv(data[1]))))
    next_departure_by_bus = dict(map(lambda bus: (bus, get_next_departure(bus, current_time)), buses))
    next_bus = min(next_departure_by_bus.keys(), key=(lambda k: next_departure_by_bus[k] - current_time))
    return next_bus * (next_departure_by_bus[next_bus] - current_time)


def get_next_departure(bus, leave_time):
    quotient = leave_time // bus
    return leave_time if quotient * bus == leave_time else quotient * bus + bus

# This code generates a question to ask Wolfram Alpha which can solve simultaneous Modulo Equations.
def solve_2(unfiltered_buses):
    t_offset_by_bus = get_t_offset_by_bus(unfiltered_buses)
    wolfram_question = 'solve '
    for entry in t_offset_by_bus.items():
        wolfram_question += f'((T + {entry[1]}) mod {entry[0]}) = '
    wolfram_question += ' 0'
    return wolfram_question

def get_t_offset_by_bus(unfiltered_buses):
    t = 0
    t_offset_by_bus = {}
    for bus in unfiltered_buses:
        if (bus != 'x'):
            t_offset_by_bus[int(bus)] = t
        t += 1
    return t_offset_by_bus

print('Part 1')
print(f'Answer: {solve_1(get_input_as_list(1))}')

print('Part 2')
print(f'Answer: {solve_2(split_csv(get_input_as_list(1)[1]))}')
