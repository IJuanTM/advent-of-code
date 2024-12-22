import os
from collections import Counter

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

# ---------------------------------------------------------------- #

# parse the input into two lists
left_list, right_list = [], []
for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

print(sum(left * Counter(right_list)[left] for left in left_list))  # 22539317