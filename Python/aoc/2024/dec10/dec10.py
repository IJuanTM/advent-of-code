from collections import deque


def part_1(data):
    score = 0
    for start in [(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val == 0]:
        visited, queue = {start}, deque([start])
        trails = set()

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and (nr, nc) not in visited:
                    if data[nr][nc] == data[r][c] + 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

                        if data[nr][nc] == 9:
                            trails.add((nr, nc))

        score += len(trails)

    return score


def part_2(data):
    rating = 0
    for start in [(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val == 0]:
        queue = deque([(start, [start])])
        trails = set()

        while queue:
            (r, c), path = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and (nr, nc) not in path:
                    if data[nr][nc] == data[r][c] + 1:
                        new_path = path + [(nr, nc)]
                        queue.append(((nr, nc), new_path))

                        if data[nr][nc] == 9:
                            trails.add(tuple(new_path))

        rating += len(trails)

    return rating


if __name__ == "__main__":
    import os

    EXPECTED = (552, 1225)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        data = [list(map(int, line.strip())) for line in f]

    result_1 = part_1(data)
    result_2 = part_2(data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
