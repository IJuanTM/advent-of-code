import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    sections = f.read().strip().split("\n\n")

offset = 10 ** 13
total = 0

for section in sections:
    lines = section.splitlines()

    a_x, a_y = [int(value[2:]) for value in lines[0].split(": ")[1].split(", ")]
    b_x, b_y = [int(value[2:]) for value in lines[1].split(": ")[1].split(", ")]
    p_x, p_y = [int(value[2:]) for value in lines[2].split(": ")[1].split(", ")]

    if offset:
        p_x += offset
        p_y += offset

    i = a_x * b_y - a_y * b_x
    j = p_x * b_y - p_y * b_x
    k = a_x * p_y - a_y * p_x

    if j % i == 0 and k % i == 0:
        total += 3 * (j // i) + (k // i)

print(total)  # 95273925552482
