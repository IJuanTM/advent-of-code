def part_1(steps):
    pos = 50
    count = sum(1 for step in steps if (pos := (pos + step) % 100) == 0)
    return count


def part_2(steps):
    pos = 50
    total = 0
    for step in steps:
        prev = pos
        new_pos = pos + step
        wraps = new_pos // 100 if new_pos >= 0 else -((-new_pos - 1) // 100 + 1)
        pos = new_pos % 100
        total += abs(wraps) - (prev == 0 and wraps < 0) + (pos == 0 and step < 0)
    return total


if __name__ == "__main__":
    import os

    EXPECTED = (1026, 5923)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        steps = [int(line[1:]) * (1 if line[0] == "R" else -1) for line in f]

    result_1 = part_1(steps)
    result_2 = part_2(steps)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
