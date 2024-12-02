import os
from collections import Counter

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()
    hands = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]

# ---------------------------------------------------------------- #

# define the lookup table and all_cards_part2
all_cards_part2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
lookup_table = {(5,): 7, (1, 4): 6, (2, 3): 5, (1, 1, 3): 4, (1, 2, 2): 3, (1, 1, 1, 2): 2, (1, 1, 1, 1, 1): 1}

# process hands
hand_types = []
for hand in hands:
    count = Counter(hand)
    if len(count) == 1 and 'J' in count:
        hand_types.append((7, hand))
        continue
    biggest_card = sorted(count, key=count.get)[-1] if sorted(count, key=count.get)[-1] != 'J' else sorted(count, key=count.get)[-2]
    count[biggest_card] += count.get('J', 0)
    count.pop('J', None)
    hand_types.append((lookup_table[tuple(sorted(count.values()))], hand))
hand_types.sort()

# group hands by type
grouped_hands = {}
for hand_type in hand_types:
    grouped_hands.setdefault(hand_type[0], []).append(hand_type[1])

# rank hands
ranks = [0] * len(hands)
rank = 1
for group in grouped_hands.values():
    group = sorted(group, key=lambda s: [all_cards_part2.index(c) for c in s])
    for hand in group:
        ranks[hands.index(hand)] = rank
        rank += 1

# calculate score
print(sum(bid * rank for bid, rank in zip(bids, ranks)))
