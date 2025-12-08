import os
from math import prod

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [line.split() for line in f]

total = sum(sum(int(lines[j][col]) for j in range(len(lines) - 1)) if lines[-1][col] == '+' else prod(int(lines[j][col]) for j in range(len(lines) - 1)) for col in range(len(lines[0])))

print(total)  # 4309240495780
