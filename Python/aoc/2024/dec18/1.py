import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    corrupted_coords = [tuple(map(int, line.strip().split(','))) for line in f]

grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

for x, y in corrupted_coords[:1024]:  # Simulate the first 1024 bytes
    grid[y][x] = '#'


def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == goal:
                return steps

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == '.':
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        steps += 1

    return -1


print(bfs((0, 0), (70, 70)))  # 294
