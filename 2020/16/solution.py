from input_utils import *
from itertools import permutations
import re
import copy
import functools


def solve(data):
    sections_search = re.search(
        "(.*)\n\nyour ticket:\n(.*)\n\nnearby tickets:\n(.*)", data, re.DOTALL)
    field_checkers = create_field_checkers(sections_search.group(1))
    ticket = list(map(int, sections_search.group(2).split(',')))
    other_tickets = map(lambda t: list(map(int, t.split(','))), sections_search.group(3).split("\n"))

    filtered_ticket_response = filter_any_field_unmappable(other_tickets, field_checkers)
    valid_tickets = filtered_ticket_response[0]
    error_rate = filtered_ticket_response[1]
    print(f'Ticket error rate: {error_rate}')

    key_ordering = determine_key_ordering(valid_tickets, field_checkers)
    labeled_ticket = dict(map(lambda item: (item[0], ticket[item[1]]), key_ordering.items()))
    product = functools.reduce(lambda i, item: i * (item[1] if item[0].startswith('departure') else 1), labeled_ticket.items(), 1)
    print(f'Product of departure fields: {product}')


def create_field_checkers(field_checkers_section):
    return dict(map(create_checker, field_checkers_section.split("\n")))


def create_checker(line):
    search = re.search("(.*): (\d*-\d*) or (\d*-\d*)", line)
    key = search.group(1)

    def func(number):
        return in_range(number, search.group(2)) or in_range(number, search.group(3))
    return (key, func)


def in_range(number, range_str):
    upper_lower = range_str.split('-')
    return number >= int(upper_lower[0]) and number <= int(upper_lower[1])


def filter_any_field_unmappable(tickets, field_checkers):
    valid_tickets = []
    error_field_values = []
    for ticket in tickets:
        invalid_field_values_for_ticket = find_invalid_field_values(ticket, field_checkers)
        error_field_values += invalid_field_values_for_ticket
        if (len(invalid_field_values_for_ticket) == 0):
            valid_tickets.append(ticket)
    return (valid_tickets, sum(error_field_values))


def find_invalid_field_values(ticket, field_checkers):
    error_field_values = []
    for field_value in ticket:
        field_value_valid = False
        for checker in field_checkers.values():
            if (checker(field_value)):
                field_value_valid = True
                break
        if (not field_value_valid):
            error_field_values.append(int(field_value))
    return error_field_values


def determine_key_ordering(tickets, field_checkers):
    can_validate = get_can_validate(tickets, field_checkers)
    order = {}
    change = True
    while(change):
        change = False
        for key, valids in copy.deepcopy(can_validate).items():
            if (len(valids) == 1):
                index = valids[0]
                order[key] = index
                for value in can_validate.values():
                    change = True
                    if (index in value):
                        value.remove(index)
    return order


def get_can_validate(tickets, field_checkers):
    can_validate = {}
    for i in range(len(tickets[0])):
        for key, checker in field_checkers.items():
            checker_can_validate_i = True
            for ticket in tickets:
                if not checker(ticket[i]):
                    checker_can_validate_i = False
                    break
            if (checker_can_validate_i):
                if (key not in can_validate):
                    can_validate[key] = []
                can_validate[key].append(i)
    return can_validate


solve(get_input(1))
