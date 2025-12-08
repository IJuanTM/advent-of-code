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
box_index = set(range(len(boxes)))
result = 0

for b1, b2, _ in sorted(distances, key=lambda x: x[2]):
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
    box_index -= connection
    if not box_index:
        result = boxes[b1][0] * boxes[b2][0]
        break

print(result)  # 8141888143
