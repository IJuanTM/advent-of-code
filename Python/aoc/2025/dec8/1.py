import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    boxes = [[int(n) for n in line.strip().split(",")] for line in f]

distances = []
for b1 in range(len(boxes)):
    for b2 in range(b1 + 1, len(boxes)):
        x1, y1, z1 = boxes[b1]
        x2, y2, z2 = boxes[b2]
        distances.append((b1, b2, (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2))

circuits = []
merged_index = set()

for i, (b1, b2, _) in enumerate(sorted(distances, key=lambda x: x[2])):
    if i == 1000:
        break
    connection = {b1, b2}
    for c in range(len(circuits)):
        if connection & circuits[c]:
            circuits[c].update(connection)
            if connection <= merged_index:
                for cc in range(len(circuits)):
                    if c != cc and connection & circuits[cc]:
                        circuits[c].update(circuits[cc])
                        circuits.pop(cc)
                        break
            break
    else:
        circuits.append(connection)
    merged_index.update(connection)

circuits.sort(key=len, reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))  # 46398
