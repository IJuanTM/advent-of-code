from functools import cache


def part_1(patterns, data):
    @cache
    def count(d):
        return d == '' or sum(count(d.removeprefix(pattern)) for pattern in patterns.split(', ') if d.startswith(pattern))

    return sum(map(bool, map(count, data)))


def part_2(patterns, data):
    @cache
    def count(d):
        return d == '' or sum(count(d.removeprefix(pattern)) for pattern in patterns.split(', ') if d.startswith(pattern))

    return sum(map(int, map(count, data)))


if __name__ == "__main__":
    import os

    EXPECTED = (251, 616957151871345)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        patterns, _, *data = f.read().splitlines()

    result_1 = part_1(patterns, data)
    result_2 = part_2(patterns, data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
