import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = [list(map(int, line.strip())) for line in f]

rating = 0
for start in [(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val == 0]:
    queue = deque([(start, [start])])
    trails = set()

    while queue:
        (r, c), path = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and (nr, nc) not in path:
                if data[nr][nc] == data[r][c] + 1:
                    new_path = path + [(nr, nc)]
                    queue.append(((nr, nc), new_path))

                    if data[nr][nc] == 9:
                        trails.add(tuple(new_path))

    rating += len(trails)

print(rating)  # 1225
