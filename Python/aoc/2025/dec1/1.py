import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    steps = [int(line[1:]) * (1 if line[0] == "R" else -1) for line in f]

pos = 50
count = sum(1 for step in steps if (pos := (pos + step) % 100) == 0)

print(count)  # 1026
