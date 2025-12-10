def part_1():
    return sum(n for start, end in ranges for n in range(start, end + 1) if len(s := str(n)) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:])


def part_2():
    return sum(n for start, end in ranges for n in range(start, end + 1) if (s := str(n)) and any(len(s) % d == 0 and s == s[:len(s) // d] * d for d in range(2, len(s) + 1)))


if __name__ == "__main__":
    import os

    EXPECTED = (30599400849, 46270373595)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        ranges = [tuple(map(int, r.split('-'))) for r in f.read().strip().split(',')]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
