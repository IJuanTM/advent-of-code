import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid = [line.rstrip('\n') for line in f]

start_col = grid[0].index('S')
beams = {start_col}
splits = 0

for row in range(1, len(grid)):
    new_beams = set()
    for col in beams:
        if grid[row][col] == '^':
            splits += 1
            if col > 0:
                new_beams.add(col - 1)
            if col < len(grid[row]) - 1:
                new_beams.add(col + 1)
        else:
            new_beams.add(col)
    beams = new_beams

print(splits)  # 1662
