import os
from collections import defaultdict
from itertools import combinations

# Read the grid from the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = f.read().split()

# Collect locations of non-empty cells
locations = defaultdict(set)
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != '.':
            locations[cell].add((r, c))

# Find antinodes
antinodes = set()
for loc_set in locations.values():
    for (r1, c1), (r2, c2) in combinations(loc_set, 2):
        dr, dc = r1 - r2, c1 - c2
        for nr, nc in [(r1 + dr, c1 + dc), (r2 - dr, c2 - dc)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                antinodes.add((nr, nc))

print(len(antinodes))  # 379
