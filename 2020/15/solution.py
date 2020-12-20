from input_utils import *


def solve(memory, elf_boredom_limit):
    last_index = {}
    for i in range(0, len(memory) - 1):
        last_index[memory[i]] = i
    for i in range(len(memory), elf_boredom_limit):
        if memory[i - 1] in last_index:
            memory.append(i - last_index[memory[i - 1]] - 1)
        else:
            memory.append(0)
        last_index[memory[i - 1]] = i - 1
    return memory[elf_boredom_limit - 1]


print('Part 1')
print(f"Answer: {solve(get_input_as_csv_ints(1), 2020)}")

print('Part 2')
print(f"Answer: {solve(get_input_as_csv_ints(1), 30000000)}")
