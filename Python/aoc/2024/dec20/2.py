import os
from itertools import combinations

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = {i + j * 1j: c for i, row in enumerate(f) for j, c in enumerate(row) if c != '#'}

start = next(p for p in grid if grid[p] == 'S')

dist = {start: 0}
queue = [start]

while queue:
    pos = queue.pop(0)
    for new_pos in [pos - 1, pos + 1, pos - 1j, pos + 1j]:
        if new_pos in grid and new_pos not in dist:
            dist[new_pos] = dist[pos] + 1
            queue.append(new_pos)

count = 0
for (p1, d1), (p2, d2) in combinations(dist.items(), 2):
    distance = abs((p1 - p2).real) + abs((p1 - p2).imag)
    if distance < 21 and d2 - d1 - distance >= 100:
        count += 1

print(count)  # 986082
