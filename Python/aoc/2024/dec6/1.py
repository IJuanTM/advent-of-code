import os

# Read input data
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = [list(line) for line in f.readlines()]

a, b = next([i, j] for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '^')
direction = [-1, 0]

count = 0

while 0 <= a < len(grid) and 0 <= b < len(grid[0]):
    if grid[a][b] != 'X':
        count += 1
        grid[a][b] = 'X'

    if 0 <= a + direction[0] < len(grid) and 0 <= b + direction[1] < len(grid[0]):
        next_field = grid[a + direction[0]][b + direction[1]]
    else:
        next_field = None

    if next_field == '#':
        direction.reverse()
        direction[1] *= -1

    a += direction[0]
    b += direction[1]

# Print result
print(count)  # 4789