import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().strip().split("\n")

a, b = len(lines), len(lines[0])
graph = {i + j * 1j: c for i, r in enumerate(lines) for j, c in enumerate(r)}

for i in range(-1, a + 1):
    graph[i - 1 * 1j] = graph[i + b * 1j] = "#"
for j in range(-1, b + 1):
    graph[-1 + j * 1j] = graph[a + j * 1j] = "#"

visited = set()
total = 0

for node in graph:
    if node not in visited and graph[node] != "#":
        stack = [(node, 1)]
        area, perimeter, sides = 0, 0, 0

        while stack:
            current, dir = stack.pop()

            if graph[current] != graph[node]:
                if graph[current + dir * 1j] == graph[node] or graph[current - dir + dir * 1j] != graph[node]:
                    perimeter += 1
                    sides += 1
                else:
                    perimeter += 1
                continue

            if current in visited:
                continue

            visited.add(current)
            area += 1

            for d in (1, -1, 1j, -1j):
                stack.append((current + d, d))

        total += area * sides

print(total)  # 830516