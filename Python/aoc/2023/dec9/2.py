import os
from operator import sub

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [list(map(int, l.split())) for l in f.read().splitlines()]


# ---------------------------------------------------------------- #

# recursive function to process the list
def f(l, pos, op):
    return op(l[pos], f([*map(sub, l[1:], l)], pos, op)) if l else 0


# calculate and print the result for part2
print(sum(f(l, 0, sub) for l in lines))
