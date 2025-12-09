def part_1(maze):
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

    while q:
        position, direction, path, score = q.pop(0)
        if (position, direction) in seen and seen[(position, direction)] < score:
            continue

        seen[(position, direction)] = score

        if position == end:
            continue

        nx, ny = position[0] + direction[0], position[1] + direction[1]
        if (nx, ny) in g and g[(nx, ny)] != '#':
            q.append(((nx, ny), direction, path | {position}, score + 1))

        q.append((position, (direction[1], -direction[0]), path, score + 1000))
        q.append((position, (-direction[1], direction[0]), path, score + 1000))

    return min(seen[(position, direction)] for (position, direction) in seen if position == end)


def part_2(maze):
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

    return len(paths) + 1


if __name__ == "__main__":
    import os

    EXPECTED = (94436, 481)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        maze = f.read().splitlines()

    result_1 = part_1(maze)
    result_2 = part_2(maze)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
