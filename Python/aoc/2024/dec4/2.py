import os

# Read and parse the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = [list(line.strip()) for line in f]

count = 0

# Iterate over all 3x3 subgrids and check both diagonals
for i in range(len(data) - 2):
    for j in range(len(data[0]) - 2):
        # Check if the subgrid contains either "MAS" or "SAM" in both diagonals
        if {''.join([data[i + k][j + k] for k in range(3)]), ''.join([data[i + k][j + 2 - k] for k in range(3)])} <= {"MAS", "SAM"}:
            count += 1

print(count)
