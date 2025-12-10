import re


def part_1():
    w, h = 101, 103
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * 100) % w
        y = (y + dy * 100) % h

        if x > w // 2 and y > h // 2:
            a += 1
        elif x > w // 2 and y < h // 2:
            b += 1
        elif x < w // 2 and y > h // 2:
            c += 1
        elif x < w // 2 and y < h // 2:
            d += 1

    return a * b * c * d


def part_2():
    min_time = None
    min_danger = float('inf')

    w, h = 101, 103

    for t in range(10000):
        a = b = c = d = 0

        for x, y, dx, dy in bots:
            x = (x + dx * t) % w
            y = (y + dy * t) % h

            if x > w // 2 and y > h // 2:
                a += 1
            elif x > w // 2 and y < h // 2:
                b += 1
            elif x < w // 2 and y > h // 2:
                c += 1
            elif x < w // 2 and y < h // 2:
                d += 1

        danger_value = a * b * c * d
        if danger_value < min_danger:
            min_danger = danger_value
            min_time = t

    return min_time


if __name__ == "__main__":
    import os

    EXPECTED = (231019008, 8280)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        bots = [list(map(int, re.findall(r'-?\d+', line))) for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
