import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    bots = [list(map(int, re.findall(r'-?\d+', line))) for line in f]

w, h = 101, 103
a = b = c = d = 0

for x, y, dx, dy in bots:
    x = (x + dx * 100) % w
    y = (y + dy * 100) % h

    if x > w // 2 and y > h // 2:
        a += 1
    elif x > w // 2 and y < h // 2:
        b += 1
    elif x < w // 2 and y > h // 2:
        c += 1
    elif x < w // 2 and y < h // 2:
        d += 1

print(a * b * c * d)  # 231019008
