import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.read().strip()

even = []
odd = []
pos = 0

for i, c in enumerate(data):
    current_range = list(range(pos, pos + int(c)))
    pos += int(c)

    if i % 2 == 0:
        even.append(current_range)
    else:
        odd.append(current_range)

for y in reversed(range(len(even))):
    for x in range(len(odd)):
        if len(odd[x]) >= len(even[y]) and even[y][0] > odd[x][0]:
            even[y] = odd[x][:len(even[y])]
            odd[x] = odd[x][len(even[y]):]

print(sum(i * j for i, even_range in enumerate(even) for j in even_range))  # 6363268339304