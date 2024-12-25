import os
from itertools import combinations

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

computers, connections = set(), set()
for line in lines:
    a, b = line.strip().split('-')
    computers.update([a, b])
    connections.update([(a, b), (b, a)])

print(sum({(a, b), (b, c), (c, a)} < connections and 't' in (a + b + c)[::2] for a, b, c in combinations(computers, 3)))  # 1227