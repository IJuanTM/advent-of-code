def part_1():
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

    return total


def part_2():
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
                current, direction = stack.pop()

                if graph[current] != graph[node]:
                    if graph[current + direction * 1j] == graph[node] or graph[current - direction + direction * 1j] != graph[node]:
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

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (1361494, 830516)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.read().strip().split("\n")

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
