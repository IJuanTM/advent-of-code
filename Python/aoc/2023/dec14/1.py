import os

# read the input and store the platform
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    platform = [list(line.strip()) for line in f]

# move 'O' upwards until blocked by a non-dot cell
for i, row in enumerate(platform):
    for j, cell in enumerate(row):
        if cell == 'O':
            current_row = i
            while current_row > 0 and platform[current_row - 1][j] == '.':
                current_row -= 1
            platform[i][j], platform[current_row][j] = platform[current_row][j], platform[i][j]

# calculate the result based on the new positions of 'O'
result = sum(len(platform) - i for i, row in enumerate(platform) for j, cell in enumerate(row) if cell == 'O')

print(result)
