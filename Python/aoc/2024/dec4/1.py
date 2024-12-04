import os

# Read and parse the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = [list(line.strip()) for line in f]

count = 0
target = "XMAS"

# Iterate through grid and check all directions
for i in range(len(data)):
    for j in range(len(data[0])):
        for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            # Check both forward and reverse directions in one step
            for direction in [1, -1]:
                if 0 <= i + direction * (len(target) - 1) * dx < len(data) and 0 <= j + direction * (len(target) - 1) * dy < len(data[0]):
                    # Check if the XMAS is present in the current direction
                    if "".join(data[i + k * direction * dx][j + k * direction * dy] for k in range(len(target))) == target:
                        count += 1

print(count)
