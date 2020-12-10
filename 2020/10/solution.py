from input_utils import *
import itertools

PREAMBLE_SIZE = 25


def solve_1(data):
    charger_list = prep_list(data)
    jumps = {}
    for i in range(1, len(charger_list)):
        jolt_diff = data[i] - data[i - 1]
        if (jolt_diff not in jumps):
            jumps[jolt_diff] = 0
        jumps[jolt_diff] += 1
    return jumps[3] * jumps[1]


def prep_list(data):
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)
    return data


def solve_2(data):
    adapters = prep_list(data)
    graph = construct_graph(adapters)
    adapters.reverse()
    paths_counter = {}
    paths_counter[adapters[0]] = 1
    for adapter in adapters:
        if (adapter not in paths_counter):
            paths_counter[adapter] = 0
        for child in graph[adapter]:
            paths_counter[adapter] += paths_counter[child]
    return paths_counter[0]


def construct_graph(adapters):
    graph = {}
    adapters_set = set(adapters)
    for adapter in adapters:
        graph[adapter] = []
        for i in range(1, 4):
            if (adapter + i in adapters_set):
                graph[adapter].append(adapter + i)
    return graph


print('Part 1')
print(f"Answer: {solve_1(get_input_as_ints(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input_as_ints(1))}")
