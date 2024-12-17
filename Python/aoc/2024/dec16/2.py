import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    maze = f.read().splitlines()

g = {}
start = None
end = None

for y, line in enumerate(maze):
    for x, c in enumerate(line):
        g[(x, y)] = c
        if c == 'S':
            start = (x, y)
        if c == 'E':
            end = (x, y)

q = [(start, (1, 0), set(), 0)]
seen = {}

best = 100000
paths = set()

while q:
    position, direction, path, score = q.pop(0)
    if (position, direction) in seen and seen[(position, direction)] < score:
        continue

    seen[(position, direction)] = score

    if position == end:
        if score < best:
            best = score
            paths.clear()
            paths.update(path)
        elif score == best:
            paths.update(path)
        continue

    nx, ny = position[0] + direction[0], position[1] + direction[1]
    if (nx, ny) in g and g[(nx, ny)] != '#':
        q.append(((nx, ny), direction, path | {position}, score + 1))

    q.append((position, (direction[1], -direction[0]), path, score + 1000))
    q.append((position, (-direction[1], direction[0]), path, score + 1000))

print(len(paths) + 1)  # 481
