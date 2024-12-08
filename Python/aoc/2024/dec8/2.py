import os
from collections import defaultdict
from itertools import combinations

# Read the grid from the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = f.read().split()

# Collect locations of non-empty cells
locations = defaultdict(set)
rows, cols = len(grid), len(grid[0])
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != '.':
            locations[cell].add((r, c))

# Find antinodes
antinodes = set()
for loc_set in locations.values():
    for (r1, c1), (r2, c2) in combinations(loc_set, 2):
        dr, dc = r1 - r2, c1 - c2

        # Extend in positive direction
        row, col = r1, c1
        while 0 <= row < rows and 0 <= col < cols:
            antinodes.add((row, col))
            row += dr
            col += dc

        # Extend in negative direction
        row, col = r2, c2
        while 0 <= row < rows and 0 <= col < cols:
            antinodes.add((row, col))
            row -= dr
            col -= dc

print(len(antinodes))  # 1339