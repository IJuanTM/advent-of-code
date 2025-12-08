import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = [line.rstrip('\n') for line in f]

start_col = grid[0].index('S')
positions = {start_col: 1}

for row in range(1, len(grid)):
    new_positions = {}
    for col, count in positions.items():
        if grid[row][col] == '^':
            if col > 0:
                new_positions[col - 1] = new_positions.get(col - 1, 0) + count
            if col < len(grid[row]) - 1:
                new_positions[col + 1] = new_positions.get(col + 1, 0) + count
        else:
            new_positions[col] = new_positions.get(col, 0) + count
    positions = new_positions

print(sum(positions.values()))  # 40941112789504
