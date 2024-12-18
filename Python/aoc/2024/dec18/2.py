import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    corrupted_coords = [tuple(map(int, line.strip().split(','))) for line in f]

grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

queue = deque([(0, 0)])
visited = {(0, 0)}

for x, y in corrupted_coords:
    grid[y][x] = '#'
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    path_found = False

    while queue:
        cx, cy = queue.popleft()

        if (cx, cy) == (70, 70):
            path_found = True
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == '.':
                queue.append((nx, ny))
                visited.add((nx, ny))

    if not path_found:
        print(f"{x},{y}")  # 31,22
        break
