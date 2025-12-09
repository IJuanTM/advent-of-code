from collections import deque


def part_1(corrupted_coords):
    grid_size = 71
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for x, y in corrupted_coords[:1024]:
        grid[y][x] = '#'

    queue = deque([(0, 0)])
    visited = {(0, 0)}
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == (70, 70):
                return steps

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == '.':
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        steps += 1

    return -1


def part_2(corrupted_coords):
    grid_size = 71
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for x, y in corrupted_coords:
        grid[y][x] = '#'
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        path_found = False

        while queue:
            cx, cy = queue.popleft()

            if (cx, cy) == (70, 70):
                path_found = True
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == '.':
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        if not path_found:
            return f"{x},{y}"

    return None


if __name__ == "__main__":
    import os

    EXPECTED = (294, "31,22")

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        corrupted_coords = [tuple(map(int, line.strip().split(','))) for line in f]

    result_1 = part_1(corrupted_coords)
    result_2 = part_2(corrupted_coords)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
