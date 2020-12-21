from input_utils import *


def solve_1(data):
    rules_text, strings_text = data.split("\n\n")
    rules = parse_rules(rules_text.split("\n"))
    strings = strings_text.split("\n")

    valid_strings = list(filter(lambda string: verify(rules, '0', string), strings))
    return len(valid_strings)


def parse_rules(lines):
    return dict(map(lambda line: line.split(": "), lines))


def parse_rule_line(rule_line):
    key, rule = rule_line.split(": ")
    return (key, [rule.replace("\"", '')] if rule.find("\"") != -1 else rule.split(' '))


def verify(rules, rule_index, string):
    return any(map(lambda match: len(match) == len(string), get_matches(rules, rule_index, string)))


def get_matches(rules, rule_index, string):
    rule = rules[rule_index]
    if (len(string) == 0):
        return ''
    elif (rule.find("\"") != -1):
        char = rule.replace("\"", '')
        return char if string[0] == char else ''
    else:
        options = rule.split(' | ')
        matches = []
        for sub_rule in options:
            sub_matches = ['']
            for sub_rule_index in sub_rule.split(' '):
                new_sub_matches = []
                for sub_match in sub_matches:
                    new_sub_matches += list(map(lambda match: sub_match + match, get_matches(rules, sub_rule_index, string[len(sub_match):])))
                sub_matches = new_sub_matches
            matches += sub_matches
        return matches


print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")

print('Part 2')
print(f"Answer: {solve_1(get_input(2))}")
