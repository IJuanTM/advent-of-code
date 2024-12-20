import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    sections = f.read().strip().split("\n\n")

total = 0

for section in sections:
    lines = section.splitlines()

    a_x, a_y = [int(value[2:]) for value in lines[0].split(": ")[1].split(", ")]
    b_x, b_y = [int(value[2:]) for value in lines[1].split(": ")[1].split(", ")]
    p_x, p_y = [int(value[2:]) for value in lines[2].split(": ")[1].split(", ")]

    min_cost = float('inf')
    found = False

    for x in range(101):
        for y in range(101):
            if x * a_x + y * b_x == p_x and x * a_y + y * b_y == p_y:
                cost = 3 * x + y
                min_cost = min(min_cost, cost)
                found = True

    if found:
        total += min_cost

print(total)  # 31552
