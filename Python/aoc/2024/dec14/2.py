import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    bots = [list(map(int, re.findall(r'-?\d+', line))) for line in f]

min_time = None
min_danger = float('inf')

w, h = 101, 103

for t in range(10000):
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * t) % w
        y = (y + dy * t) % h

        if x > w // 2 and y > h // 2:
            a += 1
        elif x > w // 2 and y < h // 2:
            b += 1
        elif x < w // 2 and y > h // 2:
            c += 1
        elif x < w // 2 and y < h // 2:
            d += 1

    danger_value = a * b * c * d
    if danger_value < min_danger:
        min_danger = danger_value
        min_time = t

print(min_time)  # 8280
