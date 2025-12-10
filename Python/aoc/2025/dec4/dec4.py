def part_1():
    rows = len(grid)
    cols = len(grid[0])

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr != 0 or dc != 0) and 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == '@')
                if adjacent < 4:
                    count += 1

    return count


def part_2():
    rows = len(grid)
    cols = len(grid[0])

    total = 0
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    adjacent = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr != 0 or dc != 0) and 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == '@')
                    if adjacent < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total += len(to_remove)

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (1489, 8890)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid = [list(line.strip()) for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
