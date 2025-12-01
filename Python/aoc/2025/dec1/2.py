import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    steps = [int(line[1:]) * (1 if line[0] == "R" else -1) for line in f]

pos = 50
total = 0
for step in steps:
    prev = pos
    new_pos = pos + step
    wraps = new_pos // 100 if new_pos >= 0 else -((-new_pos - 1) // 100 + 1)
    pos = new_pos % 100
    total += abs(wraps) - (prev == 0 and wraps < 0) + (pos == 0 and step < 0)

print(total)  # 5923
