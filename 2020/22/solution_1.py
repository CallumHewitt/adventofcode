from input_utils import *

DEBUG = False

# Pre-emptively supported more than two player. Leaving in case it becomes useful in future puzzles.
# def play_multiplayer(stacks):
#     while (len(stacks) > 1):
#         to_beat = ('x', -1)
#         competition = []
#         new_stacks = {}
#         for player, hand in stacks.items():
#             card = hand[0]
#             competition.append(card)
#             if (card > to_beat[1]):
#                 to_beat = (player, card)
#             if hand[1:]:
#                 new_stacks[player] = hand[1:]
#         new_stacks[to_beat[0]] += list(reversed(sorted(competition)))
#         stacks = new_stacks
#     return list(stacks.values())[0]

def solve_1(data):
    stacks = get_stacks(data)
    winning_stack = play_game(stacks['Player 1'], stacks['Player 2'])
    return score_stack(winning_stack)

def get_stacks(data):
    stacks = {}
    inputs = data.split("\n\n")
    for input in inputs:
        split_input = input.split("\n")
        stacks[split_input[0].replace(':', '')] = list(
            map(int, split_input[1:]))
    return stacks

def play_game(player_1_stack, player_2_stack):
    while (player_1_stack and player_2_stack):
        player_1_stack, player_2_stack = play_round(player_1_stack, player_2_stack)
    if (player_1_stack):
        return player_1_stack
    else:
        return player_2_stack

def play_round(player_1_stack, player_2_stack):
    card_1  = player_1_stack.pop(0)
    card_2  = player_2_stack.pop(0)
    if (card_1 > card_2):
        player_1_stack += [card_1, card_2]
    else:
        player_2_stack += [card_2, card_1]
    return (player_1_stack, player_2_stack)

def score_stack(stack):
    score = 0
    for i in range(len(stack)):
        score += stack[-(i + 1)] * (i+1)
    return score

def solve_2(data):
    stacks = get_stacks(data)
    _, winning_stack = play_recursive_game(stacks['Player 1'], stacks['Player 2'], 1)
    return score_stack(winning_stack)

def play_recursive_game(player_1_stack, player_2_stack, depth):
    # debug(f'=== Depth {depth} ===')
    past_rounds = set()
    player_1_stack = player_1_stack[:]
    player_2_stack = player_2_stack[:]

    while(player_1_stack and player_2_stack):
        debug(f'\n-- Round {len(past_rounds) + 1} (Depth {depth}) --')
        debug(f"Player 1's deck: {player_1_stack}")
        debug(f"Player 2's deck: {player_2_stack}")
        round = (tuple(player_1_stack), tuple(player_2_stack))
        if (round in past_rounds):
            debug(f'Played round {round} before, Player 1 wins')
            return (1, player_1_stack)
        else:
            past_rounds.add(round)

        card_1 = player_1_stack.pop(0)
        card_2 = player_2_stack.pop(0)
        debug(f'Player 1 plays {card_1}')
        debug(f'Player 2 plays {card_2}')

        if (len(player_1_stack) >= card_1 and len(player_2_stack) >= card_2):
            debug('Playing a sub-game to determine the winner...')
            winner, _ = play_recursive_game(player_1_stack[:card_1], player_2_stack[:card_2], depth + 1)
            if (winner == 1):
                debug(f'Player 1 wins round {len(past_rounds)} of depth {depth}!')
                player_1_stack += [card_1, card_2]
            else:
                debug(f'Player 2 wins round {len(past_rounds)} of depth {depth}!')
                player_2_stack += [card_2, card_1]
        else:
            if (card_1 > card_2):
                debug(f'Player 1 wins round {len(past_rounds)} of depth {depth}!')
                player_1_stack += [card_1, card_2]
            else:                
                debug(f'Player 2 wins round {len(past_rounds)} of depth {depth}!')
                player_2_stack += [card_2, card_1]
    
    if (player_1_stack):
        debug(f'The winner of depth {depth} is player 1!')
        return (1, player_1_stack)
    else:
        debug(f'The winner of depth {depth} is player 2!')
        return (2, player_2_stack)

def debug(string):
    if DEBUG: print(string) 

print('Part 1')
print(f"Answer: {solve_1(get_input(1))}")

print('Part 2')
print(f"Answer: {solve_2(get_input(1))}")