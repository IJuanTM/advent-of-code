def part_1():
    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

    return max_area


def get_size(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part_2():
    n = len(tiles)

    edges = []
    sizes = []

    for i in range(n):
        edges.append(sorted((tiles[i], tiles[i - 1])))
        for j in range(i + 1, n):
            c1, c2 = sorted((tiles[i], tiles[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any((x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2) for (x3, y3), (x4, y4) in edges):
            return size

    return 0


if __name__ == "__main__":
    import os

    EXPECTED = (4745816424, 1351617690)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        tiles = [tuple(map(int, line.strip().split(','))) for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
