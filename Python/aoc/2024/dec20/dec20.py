from itertools import combinations


def part_1(grid_data):
    grid = {i + j * 1j: c for i, row in enumerate(grid_data) for j, c in enumerate(row) if c != '#'}
    start = next(p for p in grid if grid[p] == 'S')

    dist = {start: 0}
    queue = [start]

    while queue:
        pos = queue.pop(0)
        for new_pos in [pos - 1, pos + 1, pos - 1j, pos + 1j]:
            if new_pos in grid and new_pos not in dist:
                dist[new_pos] = dist[pos] + 1
                queue.append(new_pos)

    count = 0
    for (p1, d1), (p2, d2) in combinations(dist.items(), 2):
        if abs((p1 - p2).real) + abs((p1 - p2).imag) == 2 and d2 - d1 - 2 >= 100:
            count += 1

    return count


def part_2(grid_data):
    grid = {i + j * 1j: c for i, row in enumerate(grid_data) for j, c in enumerate(row) if c != '#'}
    start = next(p for p in grid if grid[p] == 'S')

    dist = {start: 0}
    queue = [start]

    while queue:
        pos = queue.pop(0)
        for new_pos in [pos - 1, pos + 1, pos - 1j, pos + 1j]:
            if new_pos in grid and new_pos not in dist:
                dist[new_pos] = dist[pos] + 1
                queue.append(new_pos)

    count = 0
    for (p1, d1), (p2, d2) in combinations(dist.items(), 2):
        distance = abs((p1 - p2).real) + abs((p1 - p2).imag)
        if distance < 21 and d2 - d1 - distance >= 100:
            count += 1

    return count


if __name__ == "__main__":
    import os

    EXPECTED = (1365, 986082)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid_data = list(f)

    result_1 = part_1(grid_data)
    result_2 = part_2(grid_data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
