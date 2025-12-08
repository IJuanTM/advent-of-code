import os
from math import prod

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [line.rstrip('\n') for line in f]

width = max(len(line) for line in lines)
lines = [line.ljust(width) for line in lines]

total = 0
col = width - 1
nums = []

while col >= 0:
    num_str = ''.join(lines[row][col] for row in range(len(lines) - 1) if lines[row][col] != ' ')
    if num_str:
        nums.append(int(num_str))

    op = lines[-1][col]
    if op in '+*':
        total += sum(nums) if op == '+' else prod(nums)
        nums = []
        col -= 1

    col -= 1

print(total)  # 9170286552289
