def part_1():
    return sum(1 for i in ids if any(start <= i <= end for start, end in ranges))


def part_2():
    sorted_ranges = sorted(ranges)
    current_start, current_end = sorted_ranges[0]

    count = 0
    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            count += current_end - current_start + 1
            current_start, current_end = start, end

    count += current_end - current_start + 1
    return count


if __name__ == "__main__":
    import os

    EXPECTED = (888, 344378119285354)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        parts = f.read().strip().split('\n\n')
        ranges = [tuple(map(int, line.split('-'))) for line in parts[0].split('\n')]
        ids = [int(line) for line in parts[1].split('\n')]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
