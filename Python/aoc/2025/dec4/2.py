import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

total = 0
while True:
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr != 0 or dc != 0) and 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == '@')
                if adjacent < 4:
                    to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = '.'

    total += len(to_remove)

print(total)  # 8890
