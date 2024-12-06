import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.read().split("\n\n")

total = 0

for update in [list(map(int, line.split(","))) for line in data[1].splitlines()]:
    positions = {page: idx for idx, page in enumerate(update)}

    if all(positions[x] < positions[y] for x, y in [tuple(map(int, line.split("|"))) for line in data[0].splitlines()] if x in positions and y in positions):
        total += update[len(update) // 2]

print(total)
