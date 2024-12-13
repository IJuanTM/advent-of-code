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
        stack = [node]
        area, perimeter = 0, 0

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            area += 1

            for d in (1, -1, 1j, -1j):
                neighbor = current + d

                if graph[neighbor] == graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                else:
                    perimeter += 1

        total += area * perimeter

print(total)  # 1361494