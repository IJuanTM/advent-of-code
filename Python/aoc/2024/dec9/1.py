import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
    data = file.read().strip()

even = []
odd = []
pos = 0

for i, c in enumerate(data):
    c_range = list(range(pos, pos + int(c)))
    pos += int(c)

    if i % 2 == 0:
        even.append(c_range)
    else:
        odd.append(c_range)

odd_list = [i for sublist in odd for i in sublist]

for y in reversed(even):
    for x in reversed(range(len(y))):
        if odd_list and y[x] > odd_list[0]:
            y[x] = odd_list[0]
            odd_list = odd_list[1:]

print(sum(i * j for i, even_range in enumerate(even) for j in even_range))  # 6331212425418