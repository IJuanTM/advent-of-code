def part_1():
    count = 0
    target = "XMAS"

    for i in range(len(data)):
        for j in range(len(data[0])):
            for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                for direction in [1, -1]:
                    if 0 <= i + direction * (len(target) - 1) * dx < len(data) and 0 <= j + direction * (len(target) - 1) * dy < len(data[0]):
                        if "".join(data[i + k * direction * dx][j + k * direction * dy] for k in range(len(target))) == target:
                            count += 1

    return count


def part_2():
    count = 0

    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            if {''.join([data[i + k][j + k] for k in range(3)]), ''.join([data[i + k][j + 2 - k] for k in range(3)])} <= {"MAS", "SAM"}:
                count += 1

    return count


if __name__ == "__main__":
    import os

    EXPECTED = (2507, 1969)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        data = [list(line.strip()) for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
