from collections import defaultdict, deque


def part_1(data):
    total = 0

    for update in [list(map(int, line.split(","))) for line in data[1].splitlines()]:
        positions = {page: idx for idx, page in enumerate(update)}

        if all(positions[x] < positions[y] for x, y in [tuple(map(int, line.split("|"))) for line in data[0].splitlines()] if x in positions and y in positions):
            total += update[len(update) // 2]

    return total


def part_2(data):
    rules = [tuple(map(int, line.split("|"))) for line in data[0].splitlines()]
    reordered = 0

    for update in [list(map(int, line.split(","))) for line in data[1].splitlines()]:
        positions = {page: idx for idx, page in enumerate(update)}

        if not all(positions[x] < positions[y] for x, y in rules if x in positions and y in positions):
            graph = defaultdict(set)
            indegree = defaultdict(int)

            for x, y in rules:
                if x in update and y in update:
                    graph[x].add(y)
                    indegree[y] += 1

            queue = deque([page for page in update if indegree[page] == 0])
            sorted_update = []

            while queue:
                page = queue.popleft()
                sorted_update.append(page)

                for neighbor in graph[page]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            reordered += sorted_update[len(sorted_update) // 2]

    return reordered


if __name__ == "__main__":
    import os

    EXPECTED = (6612, 4944)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        data = f.read().split("\n\n")

    result_1 = part_1(data)
    result_2 = part_2(data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
