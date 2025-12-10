from collections import defaultdict
from itertools import combinations


def part_1():
    locations = defaultdict(set)
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                locations[cell].add((r, c))

    antinodes = set()
    for loc_set in locations.values():
        for (r1, c1), (r2, c2) in combinations(loc_set, 2):
            dr, dc = r1 - r2, c1 - c2
            for nr, nc in [(r1 + dr, c1 + dc), (r2 - dr, c2 - dc)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    antinodes.add((nr, nc))

    return len(antinodes)


def part_2():
    locations = defaultdict(set)
    rows, cols = len(grid), len(grid[0])
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                locations[cell].add((r, c))

    antinodes = set()
    for loc_set in locations.values():
        for (r1, c1), (r2, c2) in combinations(loc_set, 2):
            dr, dc = r1 - r2, c1 - c2

            row, col = r1, c1
            while 0 <= row < rows and 0 <= col < cols:
                antinodes.add((row, col))
                row += dr
                col += dc

            row, col = r2, c2
            while 0 <= row < rows and 0 <= col < cols:
                antinodes.add((row, col))
                row -= dr
                col -= dc

    return len(antinodes)


if __name__ == "__main__":
    import os

    EXPECTED = (379, 1339)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid = f.read().split()

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
