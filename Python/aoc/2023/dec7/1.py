import os
from collections import Counter

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()
    hands = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]

# ---------------------------------------------------------------- #

# define the lookup table and all_cards_part1
all_cards_part1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
lookup_table = {(5,): 7, (1, 4): 6, (2, 3): 5, (1, 1, 3): 4, (1, 2, 2): 3, (1, 1, 1, 2): 2, (1, 1, 1, 1, 1): 1}

# process hands
hand_types = sorted([(lookup_table[tuple(sorted(Counter(hand).values()))], hand) for hand in hands])

# group hands by type
grouped_hands = {}
for hand_type in hand_types:
    grouped_hands.setdefault(hand_type[0], []).append(hand_type[1])

# rank hands
ranks = [0] * len(hands)
rank = 1
for group in grouped_hands.values():
    group = sorted(group, key=lambda s: [all_cards_part1.index(c) for c in s])
    for hand in group:
        ranks[hands.index(hand)] = rank
        rank += 1

# calculate score
print(sum(bid * rank for bid, rank in zip(bids, ranks)))
